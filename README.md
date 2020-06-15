# BlackBox
This project is based around the Black Box puzzle/game


In Black Box, there exists an n*m grid, several "atoms" are hidden within the grid. 

Lasers are then fired into the box from the edges, these lasers interact with the atoms in a few ways: 
- If the laser hits an atom dead on it is a "hit"

```
╸╸╸╸╸╸
━━━▊╸╸
╸╸╸╸╸╸
```

- If the laser would pass next to an atom it is instead "deflected"
```
╸╸╸┃╸╸
╸╸╸┃╸╸
━━━┛╸╸
╸╸╸╸▊╸
╸╸╸╸╸╸
```

- If the laser would be deflected in both directions it is "reflected" back the way it came
```
╸╸╸╸╸╸
╸╸╸╸▊╸
━━━┫╸╸
╸╸╸╸▊╸
╸╸╸╸╸╸
```