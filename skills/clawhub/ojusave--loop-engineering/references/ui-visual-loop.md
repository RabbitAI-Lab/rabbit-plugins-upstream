# Rendered UI and Visual Design Loop

## Contents

- [Outcome](#outcome)
- [Inspect the visual system](#inspect-the-visual-system)
- [Visual hierarchy](#visual-hierarchy)
- [Layout rules](#layout-rules)
- [Component and copy rules](#component-and-copy-rules)
- [Required states](#required-states)
- [Responsive verification](#responsive-verification)
- [Visual inspection cycle](#visual-inspection-cycle)
- [Evidence](#evidence)
- [Return criteria](#return-criteria)


## Outcome

Produce an interface whose hierarchy, layout, controls, and states are clear, consistent, responsive, and visually intentional.

Inherit the parent baseline, target scenarios, guardrails, and required evidence state. Define the visible delta the rendered inspection must establish before changing the artifact.

This loop verifies the rendered artifact. It does not approve code from component structure alone.

## Inspect the visual system

Before designing or reviewing, inspect:

- existing design tokens
- typography scale
- spacing and grid
- color roles
- component primitives
- icon language
- form and feedback patterns
- responsive breakpoints
- existing adjacent screens

Reuse the established system unless it is the source of the problem.

Do not create an independent visual language for one feature.

## Visual hierarchy

The first viewport should make clear:

- where the user is
- the page or surface purpose
- the primary action
- the most important state
- the next likely step

Use typography, spacing, grouping, and placement before decorative color or containers.

## Layout rules

- Use the fewest containers needed to explain structure.
- Do not default to card grids.
- Do not add a sidebar unless persistent navigation requires it.
- Do not put every metric in a badge.
- Do not use gradients, glass effects, shadows, or oversized illustrations as substitutes for hierarchy.
- Avoid excessive rounded rectangles and nested panels.
- Keep readable line lengths.
- Align controls and labels consistently.
- Preserve density appropriate to the task.
- Avoid empty space that pushes essential actions below the fold without purpose.

## Component and copy rules

- Use familiar native or design-system controls.
- Labels should describe actions or outcomes.
- Placeholder text is not a label.
- Buttons should not use vague text such as `Continue` when the consequence can be named.
- Destructive actions must be visually and verbally distinct.
- Help text should resolve a real ambiguity.
- Tooltips should not contain essential information.

## Required states

Render relevant states, not only the happy path:

- initial
- loading or pending
- empty
- validation
- error
- permission denied
- partial completion
- success
- disabled
- destructive confirmation
- undo or recovery

State changes must be visible without relying only on color.

## Responsive verification

Inspect at least:

- one realistic narrow mobile viewport
- one realistic desktop viewport

Also inspect intermediate behavior when layout changes substantially.

Verify:

- no clipped or overflowing content
- reachable primary actions
- readable text
- usable touch targets
- logical reflow order
- tables and dense data have a mobile strategy
- dialogs fit and remain dismissible
- sticky elements do not cover content
- keyboard and zoom do not destroy layout

Do not merely shrink desktop UI.

## Visual inspection cycle

1. Start from a realistic state.
2. Capture the first viewport and primary path.
3. Identify the single highest-impact visual or comprehension failure.
4. Correct that failure.
5. Rerun the full primary path at mobile and desktop.
6. Continue only while measurable failures remain.

Do not polish low-impact details while the hierarchy or flow is wrong.

## Evidence

Record:

- viewport
- scenario
- screenshot or observed screen
- exact issue
- user impact
- change made
- rerun result

## Return criteria

Return `PASS` only after rendered inspection confirms hierarchy, states, responsive behavior, and design-system consistency.

Rendered inspection normally supports `ARTIFACT VERIFIED`. Claim `OUTCOME VALIDATED` only when representative use also shows the intended stakeholder can achieve the contracted result; do not infer that from visual polish.

Return `REWORK_REQUIRED` for a concrete visual or responsive failure.
Return `BLOCKED` when rendered inspection is unavailable; do not claim polish.
Return `NEEDS_HUMAN_JUDGMENT` when two defensible visual directions remain.
