# Item Lifespans — Expected Useful Life Data

Expected lifespan data for common household and personal items. Used as
default values by `repair_or_replace.py` when `--expected-lifespan` is not
provided.

## Major Appliances

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Refrigerator          | 14                        |
| Washing machine       | 12                        |
| Dryer (gas/electric)  | 13                        |
| Dishwasher            | 10                        |
| Oven / Range          | 15                        |
| Microwave             | 9                         |
| Freezer               | 16                        |
| Garbage disposal      | 12                        |
| Water heater (tank)   | 12                        |
| Water heater (tankless)| 20                       |

## HVAC

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Central AC unit       | 15                        |
| Furnace (gas)         | 20                        |
| Heat pump             | 15                        |
| Window AC             | 10                        |
| Air purifier          | 5                         |

## Electronics

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Laptop                | 5                         |
| Desktop computer      | 7                         |
| Smartphone            | 3                         |
| Tablet                | 4                         |
| Television (LED/OLED) | 7                         |
| Gaming console        | 6                         |
| Monitor               | 8                         |
| Router / Modem        | 5                         |
| Smartwatch            | 3                         |
| Bluetooth speaker     | 4                         |

## Small Appliances

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Coffee maker          | 5                         |
| Toaster               | 6                         |
| Blender               | 5                         |
| Vacuum cleaner        | 8                         |
| Iron                  | 6                         |
| Food processor        | 7                         |
| Air fryer             | 4                         |

## Furniture & Home

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Sofa / Couch          | 10                        |
| Mattress              | 8                         |
| Dining table          | 15                        |
| Office chair          | 7                         |
| Bookshelf             | 15                        |

## Personal Items

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Mechanical watch      | 40                        |
| Quartz watch          | 10                        |
| Eyeglasses            | 3                         |
| Bicycle               | 15                        |
| Backpack              | 5                         |
| Shoes (athletic)      | 1                         |
| Shoes (leather)       | 5                         |

## Tools & Equipment

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Power drill           | 10                        |
| Lawn mower            | 8                         |
| Pressure washer       | 7                         |
| Circular saw          | 12                        |
| Garden hose           | 5                         |

## Vehicles

| Item                  | Expected Lifespan (years) |
| --------------------- | ------------------------- |
| Car (average)         | 12                        |
| Motorcycle            | 15                        |
| Bicycle ( commuting)  | 10                        |
| E-bike                | 7                         |

## Notes

- **These are averages.** Actual lifespan varies by brand quality, usage
  frequency, maintenance, and operating environment.
- **Last quartile penalty:** Items in the last 25% of expected lifespan have
  accelerating failure rates. A 9-year-old washing machine (75% of 12-year
  lifespan) is more likely to need another repair soon than the raw percentage
  suggests.
- **Maintenance matters:** Well-maintained items can exceed these ranges
  significantly. Neglected items fail early.
- **Quality tiers:** Budget brands typically achieve 60-80% of these lifespans.
  Premium brands can exceed them by 20-40%.

## Sources

- Consumer Reports appliance lifespan studies
- National Association of Home Builders (NAHB) "Study of Life Expectancy of
  Home Components"
- EPA electronics lifecycle data
- Industry manufacturer specifications

> Lifespan data is approximate and for guidance only. Always consider the
> specific brand, model, and condition of your item.
