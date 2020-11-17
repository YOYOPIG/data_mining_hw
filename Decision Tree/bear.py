from numpy import random
import features

class Bear():
    def __init__(self):
        self.age = random.randint(0, 35)
        self.gender = features.gender[random.randint(0, 2)]
        self.height = random.normal(loc=160, scale=7)
        if self.gender=='female':
            self.weight = random.normal(loc=85, scale=12.5)
        else:
            self.weight = random.normal(loc=135, scale=32.5)
        self.habitant_area = features.habitant_area[random.randint(0, 3)]
        self.habitant_height = random.normal(loc=2000, scale=800)
        self.born_weight = random.normal(loc=325, scale=38)
        self.claw_size = random.normal(loc=4, scale=1)
        self.injury = random.choice(features.injury, 1, p=[0.1, 0.2, 0.4, 0.3])
        self.sickness = random.choice(features.sickness, 1, p=[0.1, 0.2, 0.4, 0.3])
        tmp = random.normal(loc=5, scale=2)
        if tmp<1.5:
            self.olfactory_sensation = 'bad'
        elif tmp>8.5:
            self.olfactory_sensation = 'good'
        else:
            self.olfactory_sensation = 'average'
        self.tail_length = random.normal(loc=8, scale=1)
        self.ear_size = random.normal(loc=10, scale=1)
        self.head_size = features.head_size[random.randint(0, 3)]
        self.front_paw = random.normal(loc=12, scale=1.5)
        self.rear_paw = random.normal(loc=20, scale=1.5)
        self.fur_length = random.normal(loc=8, scale=2)
        self.fur_color = features.fur_color[random.randint(0, 2)]
        self.shoulder_width = random.normal(loc=65, scale=2)
        self.food_tend = features.food_tend[random.randint(0, 3)]
        self.generate_label()
    
    def generate_label(self):
        if self.habitant_area=='zoo':
            if self.injury=='severe' or self.sickness=='severe':
                self.label = 'danger'
            else:
                self.label = 'ok'
        elif self.habitant_area=='outskirts':
            if self.olfactory_sensation=='good':
                self.label = 'ok'
            else:
                self.label = 'danger'
        else:
            if self.age<2:
                if self.born_weight<250:
                    self.label = 'danger'
                else:
                    self.label = 'ok'
            elif self.age>28:
                if self.injury=='no' or self.sickness=='no':
                    self.label = 'ok'
                else:
                    self.label = 'danger'
            else: # midage
                if self.sickness=='severe':
                    self.label = 'danger'
                elif self.sickness=='moderate':
                    if self.weight>100 and self.weight<200 and (self.injury=='mild' or self.injury=='no'):
                        self.label = 'ok'
                    else:
                        self.label = 'danger'
                else:
                    if self.injury=='severe':
                        self.label = 'danger'
                    elif self.injury=='moderate':
                        if self.weight>100 and self.weight<200:
                            self.label = 'ok'
                        else:
                            self.label = 'danger'
                    else:
                        if self.gender=='male':
                            if 160>self.height and self.height>174 and 70>self.weight and self.weight>200 and self.olfactory_sensation=='bad':
                                self.label = 'danger'
                            else:
                                self.label = 'ok'
                        else: #female
                            if 140>self.height and self.height>160 and 60>self.weight and self.weight>110 and self.olfactory_sensation=='bad':
                                self.label = 'danger'
                            else:
                                self.label = 'ok'
        return


def generate_bears(num):
    bears=[]
    for i in range(num):
        bear = Bear()
        bears.append(bear)
    return bears

bears = generate_bears(10)
for bear in bears:
    print(bear.label + ' ' + bear.habitant_area)