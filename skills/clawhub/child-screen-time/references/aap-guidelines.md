# AAP Screen Time Guidelines

## Age-Based Recommendations

The American Academy of Pediatrics (AAP) provides these evidence-based
screen time recommendations:

### Under 18 months
- **No screen time** except video chatting (e.g., with distant family)
- Brain development requires hands-on, face-to-face interaction

### 18–24 months
- **Minimal** high-quality programming only
- **Always co-view**: parents watch and discuss with the child
- Focus on educational content (e.g., Sesame Street)

### 2–5 years
- **Maximum 1 hour/day** of high-quality programming
- Co-viewing still recommended
- Avoid fast-paced content (can cause attention problems)
- No screens during meals or 1 hour before bedtime

### 6–9 years
- **~90 min/day** entertainment screen time
- Educational use is separate and encouraged
- Establish consistent limits and screen-free zones (bedroom, dinner table)
- Begin teaching digital literacy

### 10–13 years
- **~120 min/day** entertainment screen time
- Educational use continues to be separate
- Discuss online safety, cyberbullying, and responsible use
- Consider a family media plan

### 14–17 years
- **~150 min/day** entertainment screen time
- Teens need more autonomy but still need boundaries
- Focus on self-regulation skills
- Address social media's impact on mental health
- Ensure screen time doesn't replace sleep, exercise, or in-person social time

## Educational vs. Entertainment

The AAP emphasizes that **not all screen time is equal**:

- **Educational**: Khan Academy, Duolingo, coding tutorials, documentaries,
  research, creative tools (drawing/music apps) — generous or unlimited
- **Entertainment**: Games, YouTube, social media, streaming shows —
  limited by the guidelines above

## Red Flags to Watch

- Screen time replacing sleep (>1h reduction)
- Screen time replacing physical activity
- Irritability or tantrums when screens are removed
- Declining grades
- Social withdrawal
- Content that is age-inappropriate

## Sources

- AAP Council on Communications and Media (2016)
- WHO Guidelines on Physical Activity and Sedentary Behaviour (2019)
- Common Sense Media research reports

## Implementation in This Tool

The tool uses the mid-range of these recommendations as default limits:

```python
AGE_DEFAULTS = {
    range(0, 2): 0,       # Under 2: no entertainment
    range(2, 6): 60,      # 2-5: 60 min
    range(6, 10): 90,     # 6-9: 90 min
    range(10, 14): 120,   # 10-13: 120 min
    range(14, 18): 150,   # 14-17: 150 min
}
```

Parents can override any default with `set-limit`.
