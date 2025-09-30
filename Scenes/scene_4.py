def play_scene():
    """
    Scene 1: Echoes of the Forgotten Station
    - Section A: Explore or Exit
    - Section B: Follow or Ignore
    - Returns the name of the next scene or 'quit'
    """

    print("\n=== SCENE 1: Echoes of the Forgotten Station ===")
    print("You awaken to the sound of dripping water and the distant hum of electricity.")
    print("As your eyes adjust, you realize you're standing in an abandoned train station.")
    print("The walls are cracked, vines creep through shattered windows, and the air smells of rust and old memories.")
    print("A flickering sign overhead reads: 'Welcome to Station 9'—though the rest of the letters have faded into oblivion.")

    # Section A: First Choice
    while True:
        choice_a = input("\nDo you want to 'explore' the station or 'exit' immediately? ").lower().strip()
        if choice_a == "explore":
            print("\nYou step cautiously over broken tiles, peering into dusty corners.")
            print("A torn map flutters on the wall, and beneath it, a flashlight—still working. You pocket it, feeling slightly more prepared.")
            break
        elif choice_a == "exit":
            print("\nYou step outside, but the door locks behind you. A chill runs down your spine.")
            break
        else:
            print("Invalid choice. Please type 'explore' or 'exit'.")

    # Section B: Second Choice
    print("\n--- A faint sound echoes from the far end of the platform ---")
    print("It sounds like metal scraping against stone, followed by a low whisper.")

    while True:
        choice_b = input("Do you want to 'follow' the noise or 'ignore' it? ").lower().strip()
        if choice_b == "follow":
            print("\nGripping the flashlight tightly, you move toward the sound.")
            print("The corridor narrows, the walls closing in. The whisper grows louder, almost forming words.")
            print("You feel a chill run down your spine as you step into the darkness...")
            return "scene_2"
        elif choice_b == "ignore":
            print("\nYou stay put, hoping the sound passes. But something else catches your eye—a glimmer beneath the bench.")
            print("You reach for it, but the whisper returns, louder this time...")
            return "scene_2"
        else:
            print("Invalid choice. Please type 'follow' or 'ignore'.")

