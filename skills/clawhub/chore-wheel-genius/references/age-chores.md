# Age-Appropriate Chores

## Developmental Chore Guide

### Ages 2-3
**Capabilities:** Imitation, simple one-step tasks
- Pick up toys
- Put clothes in hamper
- Wipe up spills (with help)
- Feed pets (with supervision)

### Ages 4-5
**Capabilities:** Following simple instructions, desire to "help"
- Make bed (loosely)
- Set napkins/silverware on table
- Water plants
- Sort socks in laundry
- Dust low surfaces
- Clear own plate

### Ages 6-7
**Capabilities:** More independence, simple routines
- Make bed properly
- Fold and put away own clothes
- Set the table
- Sweep small areas
- Pack own school bag
- Feed pets independently
- Weed garden (with direction)

### Ages 8-10
**Capabilities:** Multi-step tasks, following checklists
- Load/unload dishwasher
- Vacuum
- Take out trash
- Clean own bedroom thoroughly
- Help with cooking (simple tasks)
- Fold laundry
- Wipe down counters
- Clean sinks

### Ages 11-13
**Capabilities:** Nearly independent, can manage own checklist
- Cook simple meals (eggs, pasta, sandwiches)
- Do own laundry completely
- Clean bathroom (sink, toilet, mirror)
- Mop floors
- Grocery shopping (with list)
- Wash the car
- Change bed sheets
- Take pets for walks

### Ages 14-17
**Capabilities:** Full chore competence, can handle any household task
- Cook full family meals
- Deep clean any room
- Yard work (mowing, raking)
- Minor home repairs
- Manage household budget for groceries
- Babysit younger siblings
- Handle trash/recycling completely

## Why Age-Appropriate Chores Matter

1. **Building competence**: Children learn life skills gradually
2. **Confidence**: Success at appropriately challenging tasks builds self-esteem
3. **Family contribution**: Everyone contributes according to ability
4. **Independence**: Chore skills transfer to adult life

## Implementation in This Tool

```python
AGE_EFFORT_CAP = {
    range(2, 4): 1,    # Only effort-1 chores
    range(4, 6): 2,    # Up to effort-2
    range(6, 8): 2,
    range(8, 11): 3,   # Up to effort-3
    range(11, 14): 4,  # Up to effort-4
    range(14, 200): 5, # All chores
}

AGE_EFFORT_MULTIPLIER = {
    range(0, 6): 0.0,
    range(6, 8): 0.3,
    range(8, 11): 0.5,
    range(11, 14): 0.7,
    range(14, 18): 0.85,
    range(18, 200): 1.0,
}
```

## Sources

- American Academy of Pediatrics (AAP) child development guidelines
- Montessori practical life curriculum
- CDC developmental milestones
