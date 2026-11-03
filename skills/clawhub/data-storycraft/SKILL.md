---
name: data-storycraft
license: MIT-0
description: Applies the Storytelling with Data method (Cole Nussbaumer Knaflic) to turn analysis into clear, decision-driving charts, slides, dashboards and reports. Use when creating, critiquing or redesigning any chart, graph, table, data slide, deck, dashboard page or written report that presents data to an audience, including requests like "plot this", "make this slide clearer", "how should I show these numbers" or "build a deck to get budget approved". Covers audience and Big Idea, chart choice, decluttering, focusing attention with color and emphasis, design, and narrative structure.
---
# Data Storycraft

Inspired by *Storytelling with Data* (Knaflic, 2015). The goal is explanatory communication: one audience, one message, one action. Every element of a visual supports the message, recedes to the background, or goes.

This is for communicating results. While the user is still exploring data, keep charts neutral and complete, because emphasis hides other patterns.

## Workflow

### 1. Context

Before any chart, write this block and put it at the top of the output:

```
Audience:  <specific person or group, ideally the decision maker>
Ask:       <what they must know or do>
Mechanism: <live presentation | sent document | both>
Big Idea:  <one sentence: point of view + what is at stake + the ask>
```

Infer what the request leaves out and say so; ask only when a wrong guess would make the work unusable. Show the data that supports the Big Idea and acknowledge the data that contradicts it.

### 2. Visual

| Need | Default |
|---|---|
| One or two numbers | The number, large, plus one sentence |
| Trend over time or continuous data | Line chart |
| Compare categories | Horizontal bar chart, sorted deliberately |
| Change between two points across categories | Slopegraph |
| Part-to-whole, survey or Likert scale | 100% stacked horizontal bar |
| Lookup by a mixed audience | Light-bordered table, or heatmap with legend |

### 3. Declutter

Remove chart border, background fill, gridlines, default markers, trailing zeros and diagonal text. Keep very light grey gridlines only if readers must trace values. Replace the legend with direct labels in the series color. Keep units on numbers ($, %, thousand separators).

### 4. Focus

Start with everything grey, then bring forward only what carries the message: one accent color (default blue; orange for negative), a thicker line, markers and value labels on the few points the message references, bold or larger text. Keep the accent to about 10% of the visual, put the most important element at the top left, and keep color meanings identical across every visual in a deck or report.

### 5. Design

Title the chart and both axes. Make the chart title an action title that states the takeaway ("Backlog has grown every month since May", not "Tickets 2024"). Annotate key points on the chart. Align title, axis titles and legend to the upper left, avoid centered text, and size the visual to its content. Put the data source in a small grey footnote.

### 6. Story

Beginning: context and tension (what is vs what could be). Middle: evidence, options, cost of inaction. End: an explicit call to action. Lead with the ask for busy or trusting audiences; go chronological when credibility or process matters. In a deck, the slide titles alone tell the story, every slide supports its title, an opening executive summary mirrors the slide titles in order, and the close restates the ask.

## Rules that hold almost always

| Rule | Why |
|---|---|
| Bar charts start at zero | The eye compares lengths; a truncated axis invents differences |
| No pie or donut charts | Angles and arcs are hard to compare; use sorted bars |
| No 3D | Perspective distorts values |
| No secondary y-axis | Label the second series directly, or split into panels sharing the x-axis |
| Consistent time intervals | Uneven spacing misrepresents the trend |
| No distorted scales or hidden contradicting data | One sharp viewer who spots it discards the whole argument |

## Reference map

Open only the reference the task needs.

| File | Open when |
|---|---|
| [reference/context.md](reference/context.md) | The brief is vague; need the Big Idea, requester questions or a storyboard |
| [reference/choosing-visuals.md](reference/choosing-visuals.md) | A need the defaults above do not cover, or notes on a default |
| [reference/decluttering.md](reference/decluttering.md) | A chart or page feels busy; grouping, alignment, contrast |
| [reference/focusing-attention.md](reference/focusing-attention.md) | Color decisions, emphasis nuances, the eyes-drawn test |
| [reference/designing.md](reference/designing.md) | Text emphasis, hierarchy, accessibility, stakeholder pushback |
| [reference/model-visuals.md](reference/model-visuals.md) | A proven recipe for a common chart |
| [reference/storytelling.md](reference/storytelling.md) | Structuring a deck, report or talk |
| [reference/worked-example.md](reference/worked-example.md) | An end-to-end example of all six steps |
| [reference/case-studies.md](reference/case-studies.md) | Dark backgrounds, live vs sent versions, ordering, tangled lines, pie replacements |
| [reference/practice-and-teams.md](reference/practice-and-teams.md) | Iterating, recurring reports, team capability |

## Output

When creating, deliver the context block, the deliverable, and one line on where the eye lands first and why.

When reviewing, use this default format:

```
Biggest problem: <one sentence>

| Lesson | Issue | Why it hurts | Fix |
(rows only for lessons with real issues: Context, Visual, Clutter, Focus, Design, Story)

Redesign: <revised visual, or a precise spec of it>
```

## Rendering charts in code

Library defaults reintroduce the clutter this method removes, so override them. A matplotlib starting point:

```python
import matplotlib.pyplot as plt

GREY, DARK, ACCENT = "#A6A6A6", "#404040", "#1F5AA6"

fig, ax = plt.subplots(figsize=(9, 5))
for name, s in df.items():                      # one column per series
    color = ACCENT if name == focus else GREY
    ax.plot(s.index, s.values, color=color, lw=3 if name == focus else 1.5)
    ax.annotate(f" {name}", (s.index[-1], s.values[-1]), color=color, va="center")
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color(GREY)
ax.tick_params(colors=GREY)
ax.grid(False)
ax.set_title("Action title that states the takeaway", loc="left", color=DARK)
ax.set_ylabel("Unit", color=GREY, loc="top")
ax.set_xlabel("Period", color=GREY, loc="left")
```

If another chart skill is also loaded, use its rendering mechanics but keep this skill's emphasis rules where the two conflict.

## Final check

Fix every "no", then check again. Deliver only when all pass.

- Is the Big Idea one sentence with an explicit ask?
- Is this the easiest chart to read for the comparison that matters?
- Does every remaining element earn its place?
- Does the eye land first on the point of the message?
- Are the chart and axes titled, with the takeaway stated in words?
- Is the accent limited, consistent across visuals and readable for colorblind viewers?
- Are elements left-aligned, text horizontal and white space kept?
- In a deck, do the titles alone tell the story, and does the executive summary mirror them?
- Do the numbers in titles and annotations match the data exactly?
