# Breathing & Relaxation Techniques — Evidence and Implementation

This document covers the breathing techniques used by Exam Stress Coach, the physiological mechanisms behind them, and implementation details for the `breathe` command.

## 1. Box Breathing (4-4-4-4 / Sama Vritti)

### What It Is

A balanced breathing pattern used by Navy SEALs and in mindfulness traditions. Each cycle has four equal phases:

1. **Inhale** for 4 seconds
2. **Hold** for 4 seconds (full lungs)
3. **Exhale** for 4 seconds
4. **Hold** for 4 seconds (empty lungs)

### Evidence

- Balances the autonomic nervous system by stimulating the vagus nerve
- Lowers cortisol levels within 5 minutes (Perciavalle et al., 2017)
- Improves heart rate variability (HRV), a key marker of stress resilience
- Used in clinical settings for panic disorder and generalized anxiety

### When to Use

- **Before studying**: Calms pre-study anxiety, sets a focused baseline
- **During study**: When you notice tension, racing thoughts, or frustration
- **Before sleep**: Helps transition to rest after evening review
- **Before the exam**: 3–5 minutes in the exam hall waiting area

### Implementation

```python
# One cycle = 16 seconds. A 5-minute session = ~18 cycles.
# The script prints phase + countdown each second.
phases = [
    ("Inhale", 4),
    ("Hold (full)", 4),
    ("Exhale", 4),
    ("Hold (empty)", 4),
]
```

## 2. The 4-7-8 Breathing Technique

### What It Is

Developed by Dr. Andrew Weil, adapted from pranayama. The extended exhale and hold create a strong parasympathetic response.

1. **Inhale** through nose for 4 seconds
2. **Hold** for 7 seconds
3. **Exhale** through mouth for 8 seconds

### Evidence

- The long exhale (8s vs 4s inhale) maximizes vagal tone
- Particularly effective for sleep onset — often called "the relaxing breath"
- Reduces sympathetic activation within 2–3 cycles

### When to Use

- **Night before exam**: When you can't fall asleep due to anxiety
- **During panic episodes**: Stronger intervention than box breathing
- **After a bad practice test**: To reset emotional state

### Implementation

```python
# One cycle = 19 seconds. A 5-minute session = ~15 cycles.
phases = [
    ("Inhale (nose)", 4),
    ("Hold", 7),
    ("Exhale (mouth)", 8),
]
```

## 3. Coherent Breathing (5.5 breaths per minute)

### What It_HE

The "resonant frequency" breathing rate (~5.5 breaths/min, or 5.5s inhale + 5.5s exhale ≈ 11s/cycle) that maximizes HRV and baroreflex sensitivity.

### Evidence

- Stephen Elliott's research on resonant frequency breathing
- Stimulates the baroreflex, which regulates blood pressure
- Associated with maximum HRV improvement at ~5.5 breaths/min
- Used in cardiac rehabilitation and PTSD treatment

### When to Use

- **Long study sessions**: As a background rhythm during breaks
- **Daily practice**: 10–20 minutes/day builds baseline stress resilience over weeks
- **Chronic stress**: More effective than box breathing for long-term regulation

### Implementation

```python
# One cycle ≈ 11 seconds (5.5s in, 5.5s out)
# The script uses whole-second approximation: 6s in, 5s out = 11s/cycle
phases = [
    ("Inhale", 6),
    ("Exhale", 5),
]
```

## General Guidelines

### Session Duration by Stress Zone

| Zone | Score | Recommended Technique | Duration |
|------|-------|-----------------------|----------|
| 🟢 Green | 1–3 | Coherent breathing (optional) | 3–5 min |
| 🟡 Amber | 4–6 | Box breathing | 3–5 min |
| 🔴 Red | 7–10 | 4-7-8 or Box | 5–10 min |

### Safety Notes

- Never force breath holds if you feel lightheaded — return to natural breathing
- 4-7-8 can cause mild tingling in the first few cycles; this is normal
- Breathing exercises are complementary to, not a replacement for, professional mental health care
- If stress scores ≥8 persist for more than 3 consecutive days, the tool recommends seeking support from a counselor or therapist

## References

1. Perciavalle, V., et al. (2017). "The role of deep breathing on stress." *Neurological Sciences*, 38(3), 451–458.
2. Lehrer, P. M., & Gevirtz, R. (2021). "Heart rate variability biofeedback." *Frontiers in Human Neuroscience*.
3. Weil, A. (2012). "Three Breathing Exercises." DrWeil.com.
4. Elliott, S. (2018). *The New Science of Breath*. Coherence Press.
5. Brown, R. P., & Gerbarg, P. L. (2005). "Sudarshan Kriya Yogic breathing in the treatment of stress, anxiety, and depression." *Journal of Alternative and Complementary Medicine*, 11(1), 189–201.
