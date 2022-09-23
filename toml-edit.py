import toml
import sys
data = toml.load('options.toml')
if len(sys.argv) < 4:
    try:
        del (data[sys.argv[1]])[sys.argv[2]]
    except KeyError:
        None
else:
    (data[sys.argv[1]])[sys.argv[2]] = sys.argv[3]
with open('options.toml', 'w') as f:
    toml.dump(data, f)