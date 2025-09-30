# scene_3.py

def play_scene():
    """
    Scene 3 (Tropical Jungle Story):
    - Section A (Choice 1): Look around or call out
    - Section B (Choice 2): Hide or push forward
    - Returns "scene_4"
    """

    print("\n=== SCENE 3 ===")
    print("You find yourself deep inside a tropical jungle. The trees tower above you,")
    print("and strange animal calls echo through the dense air. The atmosphere is humid,")
    print("and a mist creeps between the branches. You feel as if something is watching you...")

    choice_a = input("Do you want to 'look around' or 'call out'? ").lower().strip()

    if choice_a == "look around":
        print("You carefully examine your surroundings... strange footprints are visible in the mud,")
        print("as if something very large recently passed by.")
    elif choice_a == "call out":
        print("You shout into the jungle... birds scatter noisily, but then you hear leaves rustling nearby.")
    else:
        print("You hesitate, frozen in place, as the jungle grows eerily silent.")

    print("\n--- Part B of Scene 3 ---")
    print("Suddenly, you hear a heavy rustling sound. Something is moving quickly through the undergrowth...")

    choice_b = input("Do you want to 'hide' behind a massive tree or 'push forward' to face it? ").lower().strip()

    if choice_b == "hide":
        print("You slip behind a giant tree trunk... peeking through the leaves, you see a huge shadow pass by.")
        return "scene_4"
    elif choice_b == "push forward":
        print("Summoning your courage, you step deeper into the jungle... your heartbeat quickens with every step.")
        return "scene_4"
    else:
        print("You hesitate too long, but eventually your legs move forward on their own.")
        return "scene_4"
