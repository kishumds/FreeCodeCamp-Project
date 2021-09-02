# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    abbey = ["R","R","S","S","P","P","R","P","S"]
    other = ["R","S","P"]
    quincy = "P"
    la = len(opponent_history)
    l = la % 1000
    m = la // 1000
    
    start = m * 1000
    finish = m * 1000 + 4

    key = opponent_history[start:finish]
    
    if l < 4:
      return other[l % 3]
    else:
      if key == ["","P","R","S"]:
        return other[l % 3]
      elif key == ["","R","R","R"]:
        return other[l % 3]
      elif key == ["","R","P","P"]:
        return quincy
      else:
        return abbey[l % 9]