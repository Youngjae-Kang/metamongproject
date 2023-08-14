import time

def start_game():
    print("1860년대 무더운 여름. 당신은 가난한 법학생 라스꼴리니꼬프입니다. 나는 대중을 비범한 사람과 평범한 사람으로 분류합니다. 세상을 변화시키는 쪽은 비범한 사람이라고 생각합니다. 그들은 목적을 이루기 위해 어떤 수단이든 사용할 수 있다고 믿고, 심지어는 생명을 빼앗을 권리까지 있다고 여깁니다. 나 또한 남들보다 뛰어난 지성을 가진 사람이라고 생각합니다. 이런 당신의 사상은 전당포 주인 노파를 사회의 악으로 여기고 그를 죽이기로 결심하게 된 동기가 되었습니다. 노파를 제거함으로써 가난한 사람들이 더 나은 삶을 살 수 있을 것이라 믿게 되고, 당신은 살인을 계획하게 되었습니다.")
    time.sleep(2)
    print("당신은 세상을 변화시키고자 하는 비범한 사람이며, 노파를 제거하기로 결심했습니다.")
    time.sleep(2)
    print("하지만 살인 계획을 세운 뒤 현장에서 불안한 기분이 드는데...")
    time.sleep(2)
    print("당신은 어떤 선택을 하겠습니까?")

    choice = input("1. 계획을 계속 진행한다.\n2. 계획을 포기한다.\n선택: ")

    if choice == "1":
        continue_plan()
    elif choice == "2":
        abandon_plan()
    else:
        print("올바른 선택을 입력하세요.")
        start_game()

def continue_plan():
    print("당신은 계획을 이어서 진행합니다. 전당포 주인과의 마주침에서 어색함이 느껴집니다.")
    time.sleep(2)
    print("당신은 어떤 선택을 하겠습니까?")

    choice = input("1. 계획대로 살인을 실행한다.\n2. 살인 현장을 빠져나간다.\n선택: ")

    if choice == "1":
        commit_murder()
    elif choice == "2":
        escape_murder_scene()
    else:
        print("올바른 선택을 입력하세요.")
        continue_plan()

def abandon_plan():
    print("당신은 계획을 포기하고 현장을 떠났습니다. 그러나 어떤 선택을 할지 계속 고민합니다.")
    time.sleep(2)
    print("당신은 어떤 선택을 하겠습니까?")

    choice = input("1. 다시 계획을 세우기로 한다.\n2. 다른 길을 찾아본다.\n선택: ")

    if choice == "1":
        continue_plan()
    elif choice == "2":
        find_alternative()
    else:
        print("올바른 선택을 입력하세요.")
        abandon_plan()

def commit_murder():
    print("당신은 계획대로 살인을 실행합니다. 그러나 예기치 못한 일이 벌어집니다.")
    time.sleep(2)
    print("살인범의 동생까지 살해되었고, 어떤 선택을 하겠습니까?")

    choice = input("1. 현장을 빠져나간다.\n2. 자수한다.\n선택: ")

    if choice == "1":
        escape_murder_scene()
    elif choice == "2":
        confess_to_murder()
    else:
        print("올바른 선택을 입력하세요.")
        commit_murder()

def escape_murder_scene():
    print("당신은 살인 현장에서 빠져나옵니다. 그러나 불안한 기분이 계속 남아있습니다.")
    time.sleep(2)
    print("당신은 무엇을 하겠습니까?")

    choice = input("1. 숨는다.\n2. 일상 생활로 돌아간다.\n선택: ")

    if choice == "1":
        hide_out()
    elif choice == "2":
        return_to_normal_life()
    else:
        print("올바른 선택을 입력하세요.")
        escape_murder_scene()

def confess_to_murder():
    print("당신은 살인을 자백합니다. 경찰에게 체포되어 수감됩니다.")
    time.sleep(2)
    print("당신의 선택에 따라 이야기의 결말이 달라집니다.")

    time.sleep(1)
    print("\n=== 결말 1: 자수한 결말 ===")
    time.sleep(2)
    print("판사 뽀르피리의 제안에 따라 가벼운 형량을 받아 시베리아로 갈 수 있게 되었습니다.")
    time.sleep(2)
    print("소냐와 함께 시베리아로 떠나, 새로운 삶을 시작합니다.")
    time.sleep(2)
    print("이야기는 여기까지 입니다.\n")

    time.sleep(1)
    print("\n=== 결말 2: 자백한 결말 ===")
    time.sleep(2)
    print("당신의 자백으로 인해 징역 8년의 형을 받게 되었습니다.")
    time.sleep(2)
    print("소냐도 가족의 생계문제가 해결되어 시베리아로 떠납니다.")
    time.sleep(2)
    print("소냐와 함께 시베리아로 떠나, 새로운 삶을 시작합니다.")
    time.sleep(2)
    print("이야기는 여기까지 입니다.\n")

def hide_out():
    print("당신은 숨기로 결정합니다. 그러나 불안한 마음은 여전합니다.")
    time.sleep(2)
    print("당신은 어떤 선택을 하겠습니까?")

    choice = input("1. 자수한다.\n2. 계속 숨는다.\n선택: ")

    if choice == "1":
        confess_to_murder()
    elif choice == "2":
        continue_hiding()
    else:
        print("올바른 선택을 입력하세요.")
        hide_out()

def continue_hiding():
    print("당신은 계속해서 숨기로 결정합니다. 불안한 일상이 계속됩니다.")
    time.sleep(2)
    print("당신은 어떤 선택을 하겠습니까?")

    choice = input("1. 자수한다.\n2. 계속 숨는다.\n선택: ")

    if choice == "1":
        confess_to_murder()
    elif choice == "2":
        continue_hiding()
    else:
        print("올바른 선택을 입력하세요.")
        continue_hiding()

def return_to_normal_life():
    print("당신은 일상 생활로 돌아갑니다. 그러나 어떤 선택을 할지 고민합니다.")
    time.sleep(2)
    print("당신은 어떤 선택을 하겠습니까?")

    choice = input("1. 다시 계획을 세우기로 한다.\n2. 더 나은 길을 찾는다.\n선택: ")

    if choice == "1":
        continue_plan()
    elif choice == "2":
        find_alternative()
    else:
        print("올바른 선택을 입력하세요.")
        return_to_normal_life()

def find_alternative():
    print("당신은 더 나은 선택을 찾기로 결정합니다. 어떤 길을 선택하겠습니까?")

    choice = input("1. 소냐를 찾아가서 다른 방법을 모색한다.\n2. 다른 사람들에게 도움을 청한다.\n선택: ")

    if choice == "1":
        seek_help_from_sonya()
    elif choice == "2":
        ask_for_help()
    else:
        print("올바른 선택을 입력하세요.")
        find_alternative()

def seek_help_from_sonya():
    print("소냐를 찾아가서 상황을 얘기하며 다른 방법을 모색합니다.")
    time.sleep(2)
    print("소냐와의 대화를 통해 새로운 길을 찾게 됩니다.")
    time.sleep(2)
    print("당신의 선택에 따라 이야기의 결말이 달라집니다.")

    time.sleep(1)
    print("\n=== 결말 3: 소냐의 도움 결말 ===")
    time.sleep(2)
    print("소냐의 도움을 받아 노파를 변화시키는 더 나은 방법을 찾습니다.")
    time.sleep(2)
    print("소냐와 함께 노력하여 사회의 변화를 이루어냅니다.")
    time.sleep(2)
    print("이야기는 여기까지 입니다.\n")

def ask_for_help():
    print("당신은 다른 사람들에게 도움을 청하려 합니다.")
    time.sleep(2)
    print("다양한 사람들과의 대화를 통해 새로운 길을 모색합니다.")
    time.sleep(2)
    print("당신의 선택에 따라 이야기의 결말이 달라집니다.")

    time.sleep(1)
    print("\n=== 결말 4: 다른 사람들의 도움 결말 ===")
    time.sleep(2)
    print("다른 사람들의 도움을 받아 노파를 변화시키는 더 나은 방법을 찾습니다.")
    time.sleep(2)
    print("여러 사람들과 함께 노력하여 사회의 변화를 이루어냅니다.")
    time.sleep(2)
    print("이야기는 여기까지 입니다.\n")

# 게임 시작
start_game()
