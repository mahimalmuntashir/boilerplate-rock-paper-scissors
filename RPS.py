# The example function kept track of the opponent's history and played whatever the opponent played two plays ago. It is not a good player so I changed the code to pass the challenge.
# Keep track of patterns in the opponent's history and play whatever the opponent is most likely to play based on their previous playing history.
# Mahim Al Muntashir Billah
# BSc in Computer Science and Technology
# Nantong University, China.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    
    num_rounds = len(opponent_history)
    guess = "R"
    pattern_size = 7
    pattern_next_counts = {}

    if num_rounds < pattern_size:
        return guess
    
    for i in range(num_rounds - pattern_size):
        pattern = tuple(opponent_history[i:i+pattern_size])
        next_play = opponent_history[i+pattern_size]
        
        if pattern not in pattern_next_counts:
            pattern_next_counts[pattern] = {}
        if next_play not in pattern_next_counts[pattern]:
            pattern_next_counts[pattern][next_play] = 0
        
        pattern_next_counts[pattern][next_play] += 1

    last_pattern = tuple(opponent_history[-pattern_size:])
    if last_pattern not in pattern_next_counts:
        return guess

    next_play_counts = pattern_next_counts[last_pattern]
    predicted_next_play = max(next_play_counts, key=next_play_counts.get)

    counter_play = {"R": "P", "P": "S", "S": "R"}
    guess = counter_play[predicted_next_play]

    return guess