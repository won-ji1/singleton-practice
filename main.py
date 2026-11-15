from singleton import Singleton

a = Singleton()
b = Singleton()

print("== 동일 인스턴스 비교 ==")
print(f"a is b : {a is b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")

print("\n== 상태 공유 확인 ==")
a.counter = 10
print("a.counter = 10 으로 변경")
print(f"b.counter = {b.counter}")