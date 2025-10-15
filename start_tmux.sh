 #!/bin/bash

exec > /home/pi/tmux_debug.log 2>&1
set -x


# Session name
SESSION="autostart"

# Path to your Documents folder
DOCS="$HOME/Documents"

# Python and SuperCollider files
PY1="motionDetect.py"
PY2="servoDriver.py"
SC="oscServoMotionDetect.scd"


# Path to virtual environment in /home/pi/.venv
VENV="$HOME/.venv/bin/activate"
SCLANG="/usr/local/bin/sclang"   # <-- update this with the output of `which sclang`

# Kill old session if it exists (prevents duplicates)
tmux kill-session -t $SESSION 2>/dev/null

# Start new tmux session with Python file 1 in venv
tmux new-session -d -s $SESSION -c "$DOCS" "bash -i -c 'source $VENV && python3 $PY1'"

# Create second window for Python file 2 in venv

tmux new-window -t $SESSION:1 -c "$DOCS" "bash -i -c 'source $VENV && python3 $PY2'"

# Create third window for SuperCollider file

tmux new-window -t $SESSION:2 -c "$DOCS" "bash -i -c 'sleep 5 && $SCLANG $SC || echo sclang failed; exec bash'"


echo "All tmux windows started at $(date)"
# Optional: attach automatically (only if you want to see it on boot)
# tmux attach -t $SESSION
