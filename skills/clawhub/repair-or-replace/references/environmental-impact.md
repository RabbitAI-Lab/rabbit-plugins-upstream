# Environmental Impact — E-Waste and Sustainability

The environmental factor in the Repair or Replace decision matrix accounts for
two considerations: avoiding e-waste through repair, and the energy efficiency
gains of newer models.

## The E-Waste Problem

### Scale

- The world generates **~57 million tonnes** of e-waste annually (UN Global
  E-waste Monitor, 2021).
- Only **~17%** is formally collected and recycled.
- E-waste contains toxic materials (lead, mercury, cadmium) that leach into
  soil and water when landfilled.

### Embodied Carbon

Every manufactured product carries "embodied" carbon — the emissions from
extraction, manufacturing, transport, and packaging:

| Item                | Embodied CO2 (kg)  | Equivalent            |
| ------------------- | ------------------ | --------------------- |
| Smartphone          | ~70                | 300 km of driving     |
| Laptop              | ~200               | 1,000 km of driving   |
| Washing machine     | ~400               | 2,000 km of driving   |
| Refrigerator        | ~500               | 2,500 km of driving   |
| Television (55")    | ~300               | 1,500 km of driving   |

Repairing extends the useful life of these embodied emissions. Keeping a
laptop for 5 years instead of 3 reduces its annual carbon footprint by ~40%.

### Right to Repair

The Right to Repair movement advocates for:
- Access to repair manuals and schematics
- Availability of spare parts
- No software locks preventing third-party repair
- Modular designs that are easy to disassemble

Supporting repair — even when slightly more expensive — signals market demand
for repairable products.

## When Replacement Is More Environmental

### Energy Efficiency Gains

For energy-hungry appliances, a new model may be significantly more efficient:

| Appliance          | Efficiency Gain (10-year-old → new) |
| ------------------ | ------------------------------------ |
| Refrigerator       | 20-40% more efficient                |
| Washing machine    | 25-50% more efficient                |
| Dishwasher         | 20-30% more efficient                |
| Air conditioner    | 30-50% more efficient                |
| Water heater       | 15-30% more efficient                |

### The Break-Even Calculation

The environmental benefit of replacement depends on whether the energy savings
offset the embodied carbon of the new item:

```
years_to_break_even = new_item_embodied_carbon / annual_energy_savings_carbon
```

**Example:** A new refrigerator saves ~100 kg CO2/year in energy. The new
fridge has ~500 kg embodied CO2. Break-even: 5 years. If the old fridge has
no remaining life, replace. If it has 5+ years left, repair is better.

### Rule of Thumb

- **Electronics (phones, laptops):** Almost always repair. Embodied carbon is
  high relative to energy savings.
- **Major appliances:** Compare. If the old unit is 10+ years old, replacement
  may save more carbon through efficiency.
- **Small appliances:** Usually repair. Low embodied carbon, low efficiency
  gains.

## Recycling and Disposal

### If You Replace

When replacing an item, ensure the old one is disposed of responsibly:

1. **Donate** if still functional — many charities, schools, and community
   centers accept working electronics and appliances.
2. **E-waste recycling** — use certified e-waste recyclers (e-STEWARDS,
   R2v3 certified). Do NOT put electronics in regular trash.
3. **Manufacturer takeback** — many manufacturers (Apple, Dell, Best Buy)
   have free recycling programs.
4. **Battery removal** — remove batteries before disposal; they require
   separate recycling.

### If You Recycle (Beyond Repair)

When the decision is "Recycle/Donate" (item beyond economic repair):

1. **Data wipe** — for electronics, securely erase all data before disposal.
2. **Parts harvesting** — some repair shops buy non-functional units for parts.
3. **Certified recycler** — ensure the recycler doesn't ship waste to
   developing countries (a common illegal practice).

## Scoring in This Skill

The environmental factor in `repair_or_replace.py` works as follows:

| Scenario                              | Environmental Score |
| ------------------------------------- | ------------------- |
| Repair, no efficiency data            | 20/20 (full repair) |
| Repair, replacement is more efficient | 12-20/20 (partial)  |
| Replace for efficiency reasons        | 0-8/20 (replacement) |

If you know the efficiency gain of a replacement, supply it with
`--efficiency-gain <percent>` for a more accurate score.

## Further Reading

- [UN Global E-waste Monitor](https://ewastemonitor.info/)
- [iFixit Repair Guides](https://www.ifixit.com/Guide)
- [EPA Electronics Donation and Recycling](https://www.epa.gov/recycle/electronics-donation-and-recycling)
- [Repair Café International](https://repaircafe.org/)
