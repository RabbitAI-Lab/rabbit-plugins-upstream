---
name: ikea-instruction-reader
description: "Decode, track, and guide through furniture assembly instructions from step diagrams. Manages parts inventory, tracks assembly progress, identifies the current step from a photo, and warns about common mistakes. Use when assembling flat-pack furniture or following visual-only instruction manuals."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [furniture, assembly, ikea, diy, instructions, flat-pack]
---

# IKEA Instruction Reader

## Overview

Flat-pack furniture manuals are famously wordless — they use only line drawings with numbered steps, no text. This skill helps users navigate these manuals by: tracking which parts and hardware have been used, identifying which step a user is on from a photo, providing verbal guidance for each step, warning about common mistakes (like inserting cam locks backwards), and maintaining a progress tracker. It turns a frustrating "stare at the picture" experience into a guided assembly.

## When to Use

- A user is **assembling flat-pack furniture** (IKEA, Wayfair, Target, etc.) and needs help understanding the instructions
- A user wants to **verify they have all parts** before starting
- A user needs to **identify which step** they're on from a photo of their progress
- A user is **stuck** on a particular step and needs it explained in words
- A user wants a **pre-assembly checklist** of tools needed
- **Don't use for:** furniture that comes fully assembled, or video tutorials (this is for printed/diagram-based instructions)

## Core Features

### 1. Parts Tracker (`scripts/assembly_tracker.py`)
Tracks all parts and hardware throughout the assembly process:
- Initialize from a manifest (part numbers, quantities, descriptions)
- Check off parts as they're used per step
- Flag missing parts before you reach the step that needs them
- Generate a "completion percentage" estimate

### 2. Step Guide (`scripts/step_guide.py`)
Provides text guidance for diagram-only steps:
- Translates visual actions into written instructions
- Highlights common mistakes per step type
- Generates a tool checklist for the whole project

## Numbered Workflow

1. **Inventory check:** List all parts and hardware before starting. Verify quantities match the manifest.
2. **Tool prep:** Identify all tools needed (Allen key, screwdriver, hammer, etc.) and gather them.
3. **Step-by-step guidance:** For each step, read the parts used, the action, and any warnings.
4. **Progress tracking:** Mark each step complete and check off parts used.
5. **Error prevention:** Warn about orientation mistakes, wrong hardware, skipped steps.

## Common Pitfalls

1. **Cam lock orientation.** Cam locks must be inserted with the arrow pointing toward the corresponding dowel. Inserting backwards is the #1 assembly error. Always check the arrow direction.

2. **Wood dowel vs. cam lock confusion.** Dowels go into pre-drilled holes for alignment; cam locks secure joints. They look similar in diagrams. Check the diameter.

3. **Left/right panel confusion.** Many furniture pieces have a "good side" facing out. Diagrams show this with a subtle texture difference. When in doubt, the finished edge faces away from the wall/back.

4. **Not pre-sorting hardware.** IKEA bags hardware by type, but mixing them on the work surface leads to using the wrong screw. Sort by type before starting.

5. **Skipping the wall-anchor step.** Bookcases and dressers MUST be anchored to the wall for safety. This step is often at the end and easy to skip.

## Verification Checklist

- [ ] All parts counted and matched to manifest
- [ ] Required tools gathered before starting
- [ ] Hardware sorted by type
- [ ] Each step's parts checked off after use
- [ ] Cam lock arrows verified before tightening
- [ ] Wall anchor installed (for tall furniture)

## Example Session

**User:** "I'm assembling a KALLAX shelf. I have the manual open to step 3 but I'm confused."

**Agent:** Based on common KALLAX assembly patterns, step 3 typically involves connecting the side panels to the top/bottom using wooden dowels and cam locks. Let me guide you:

1. Insert 8 wooden dowels into the pre-drilled holes on the top panel edges
2. Place the side panels onto the dowels
3. Insert cam locks into the round holes — **arrow pointing toward the dowel**
4. Tighten cam locks clockwise with a screwdriver until snug
5. Parts used this step: 2× side panels, 1× top panel, 8× dowels, 8× cam locks

Would you like me to track these parts as used?
