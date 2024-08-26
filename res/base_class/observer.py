from typing import List

class Observer:
    """
    관찰자

    구독자(Subscriber)에게 뭔가 반응이 생기면 update 함수 실행함

    사용 가능한 메서드:
    - update
    """
    def __init__(self):
        pass

    def update(self):
        print("이거 이대로 쓰지 말고 다시 작성 합시당")


class Subscriber:
    """
    구독자
    
    반응이 생기면 관찰자(Observer)에게 알려줌\n
    그럼 관찰자는 update 함수 실행

    사용 가능한 메서드:
    - addObserver
    - removeObserver
    - notify
    """
    def __init__(self):
        self.subscriber: List[Observer] = []

    def addObserver(self, observer: Observer):
        self.subscriber.append(observer)

    def removeObserver(self, observer: Observer):
        self.subscriber.remove(observer)

    def notify(self):
        for sub in self.subscriber:
            sub.update()