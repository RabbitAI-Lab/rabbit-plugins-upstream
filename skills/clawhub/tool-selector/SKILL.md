---
name: tool-selector
description: "Describe a DIY project, get an exact tool list, materials needed, cost estimate, and step-by-step guide filtered by your available tools. Recommends the right tool for each job, finds substitutions, and flags missing tools. Use when planning any DIY, home repair, or making project."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [diy, tools, home-repair, projects, woodworking, maker]
---

# Tool Selector

## Overview

Every DIY project starts with the same question: "What do I need?" Most people either overbuy (spending 3× too much on tools they'll use once) or underestimate (making 3 trips to the hardware store mid-project). This skill takes a project description — "build a raised garden bed", "fix a leaky faucet", "install a ceiling fan" — and generates: the exact tools needed with alternatives, a materials list with quantities, a cost estimate, and a step-by-step plan that works with the tools you already have.

## When to Use

- A user wants to **start a DIY project** but doesn't know what tools they need
- A user is at the **hardware store** and wants to verify their shopping list is complete
- A user wants to know **what tool to use for a specific task** (e.g., "what drill bit for brick?")
- A user has **limited tools** and needs to know if they can do a project without buying more
- A user wants a **cost estimate** for a project before committing
- **Don't use for:** professional construction estimating (too simplified), or purely electrical/plumbing work requiring licensed professionals

## Core Features

### Project Planner (`scripts/project_planner.py`)
The main tool that generates complete project plans:
- Searches a built-in database of 50+ common DIY projects
- Returns tools, materials, estimated time, difficulty, and step-by-step instructions
- Filters tool recommendations by what the user already owns
- Suggests substitutions when a tool is missing

### Tool Substitution Guide (`scripts/tool_substitution.py`)
Finds alternative tools when you don't have the exact one:
- "Don't have a miter saw? Use a circular saw with a speed square"
- "No pipe wrench? Adjustable pliers work for small pipes"
- Rates substitutions by quality (exact match → good → workable → last resort)

## Numbered Workflow

1. **Describe the project** — natural language description ("install a towel rack", "build a bookshelf")
2. **Specify available tools** — list what you already own (optional but recommended)
3. **Get the plan** — tools needed, materials, cost, steps
4. **Review substitutions** — for any missing tools, see alternatives
5. **Shop with confidence** — complete shopping list with quantities

## Common Pitfalls

1. **Underestimating fasteners.** Most DIY projects need 20% more screws/nails than you think. The planner adds a buffer automatically.

2. **Ignoring safety gear.** Safety glasses, dust mask, and gloves are needed for almost every project. The planner always includes them.

3. **Wrong tool for the material.** Drilling into masonry needs a hammer drill and masonry bits; regular drill bits will burn out. The planner matches tools to materials.

4. **Forgetting about finishing.** Sandpaper, primer, paint, and brushes are easy to forget but necessary. The planner includes finishing supplies.

5. **Not accounting for tool quality tiers.** A $15 circular saw and a $150 circular saw do different jobs. The planner offers budget and quality tiers.

## Verification Checklist

- [ ] All required tools listed with alternatives
- [ ] Material quantities include waste buffer (10-20%)
- [ ] Safety gear included
- [ ] Cost estimate ranges from budget to quality
- [ ] Step-by-step uses only available or substitutable tools

## Example Session

**User:** "I want to build a raised garden bed that's 4x8 feet. I have a drill, circular saw, and measuring tape."

**Agent:**
```
📊 PROJECT: Raised Garden Bed (4'×8'×1')
⏱️ Estimated time: 2-3 hours
🎯 Difficulty: Beginner

TOOLS NEEDED:
  ✓ Cordless drill (you have this)
  ✓ Circular saw (you have this)
  ✓ Measuring tape (you have this)
  🔲 Speed square — $8 (for straight cuts)
  🔲 Phillips drill bit set — $12

MATERIALS:
  • 4× cedar 2×6 boards, 8ft long — $48
  • 2× cedar 2×4 boards, 8ft (for corners) — $14
  • 1 box exterior screws (3") — $8
  • 12 cu ft potting soil — $30
  • Landscape fabric — $5

ESTIMATED COST: $125 (tools) + $105 (materials) = $125 total*
  *You already own $0 worth of required tools.

STEPS:
  1. Cut boards to size: 4× side panels at 4ft, 2× end panels at 8ft
  2. Cut 4× corner posts from 2×4 at 12" each
  3. Pre-drill holes to prevent splitting
  4. Attach side panels to corner posts with 3" exterior screws
  5. Line bottom with landscape fabric
  6. Fill with potting soil
```
