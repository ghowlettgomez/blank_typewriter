#include <Servo.h>

#define MAX_STEPS 200.0

#define S1_PIN 5
#define S2_PIN 6

typedef struct move_queue_node move_queue_node_t;

struct move_queue_node {
  int a1, a2;
  move_queue_node_t *next;
};

move_queue_node_t *head, *tail;

Servo s1, s2;

float demo_set[][2] = {
  {90, 0},
  {90, 0},
  {90, 0},
  {90, 0}
};

int curr = 0;

void setup() {
  while (!Serial);
  Serial.begin(9600);

  s1.attach(S1_PIN);
  s2.attach(S2_PIN);

  head = (move_queue_node_t *)malloc(sizeof(move_queue_node_t));
  head->a1 = s1.read();
  head->a2 = s2.read();
  head->next = NULL;

  move_queue_node_t *curr;
  move_queue_node_t *prev = head;
  for (int i = 0; i < 4; i++) {
    curr = (move_queue_node_t *)malloc(sizeof(move_queue_node_t));
    curr->a1 = demo_set[i][0];
    curr->a2 = demo_set[i][1];
    curr->next = NULL;

    Serial.print(curr->a1);
    Serial.print(", ");
    Serial.println(curr->a2);

    prev->next = curr;
    prev = curr;
  }

  curr = head;
  while (curr->next != NULL) {
    curr = curr->next;
  }
  tail = curr;
}

void loop() {
  if (Serial.available() > 0) {
    int a1_temp = Serial.parseInt();
    int a2_temp = Serial.parseInt();
    if (a1_temp > 5 && a2_temp > 5) {
      tail->next = (move_queue_node_t *)malloc(sizeof(move_queue_node_t));
      tail->next->a1 = a1_temp;
      tail->next->a2 = a2_temp;
      tail->next->next = NULL;
      tail = tail->next;
    }
  }
  if (head->next != NULL) {
    float a1_step = (head->next->a1 - head->a1) / MAX_STEPS;
    float a2_step = (head->next->a2 - head->a2) / MAX_STEPS;
    for (int i = 0; i < MAX_STEPS - 1; i++) {
      s1.write(head->a1 + a1_step * i);
      s2.write(head->a2 + a2_step * i);
      delay(20);
    }
    s1.write(head->next->a1);
    s2.write(head->next->a2);

    move_queue_node_t *tmp = head->next;
    free(head);
    head = tmp;
  }
}