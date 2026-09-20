# Accessibility Loop

## Outcome

Ensure the relevant user flow is perceivable, operable, understandable, and robust for keyboard, assistive technology, zoom, contrast, motion, and varied input needs.

Inherit the parent baseline, target scenario, guardrails, and required evidence state. Record which user need, input mode, and task path the checks actually observe.

Accessibility is not a final checkbox and not equivalent to an automated scan.

## Inspect

Review the actual rendered flow and source for:

- semantic structure
- heading order
- landmarks
- control names and roles
- label associations
- keyboard order
- focus visibility and management
- dialogs and overlays
- error identification
- status announcements
- contrast
- color dependence
- zoom and reflow
- motion
- target size
- media alternatives
- table structure

Prefer native HTML and existing accessible primitives.

## Keyboard scenario

Complete the primary path using keyboard only.

Verify:

- every interactive element is reachable
- focus order follows the task
- focus is visible
- no keyboard traps
- menus, dialogs, tabs, and popovers follow expected patterns
- focus moves meaningfully after open, close, submit, error, and navigation
- escape and cancellation work where expected

## Screen-reader-oriented inspection

When screen-reader tooling is available, exercise the relevant path. Otherwise inspect the accessibility tree or semantics and report the limitation.

Verify:

- names match visible purpose
- roles and states are exposed
- errors are associated with fields
- dynamic status is announced when necessary
- decorative content is hidden appropriately
- headings and landmarks support navigation

## Visual accessibility

Verify:

- text and control contrast
- information is not encoded by color alone
- focus indicator contrast
- 200 percent zoom and reflow where relevant
- text spacing does not break the layout
- motion respects reduced-motion preferences
- touch targets are usable

## Automated tools

Use available scanners or linters as evidence, not as the only verifier.

Record tool output and manually inspect the primary scenario.

## Fix order

Prioritize:

1. Blocked task completion
2. Missing names, labels, or semantics
3. Keyboard traps or focus loss
4. Errors and dynamic state not communicated
5. Contrast, zoom, or responsive barriers
6. Lower-impact enhancements

## Return criteria

Return `PASS` when relevant automated checks and manual scenarios pass with no material barrier.

Report `OUTCOME VALIDATED` only when the target task is completed through the relevant input or assistive-technology scenario. When only source, semantics, lint, or scanner evidence is available, report `ARTIFACT VERIFIED` and name the unobserved scenario.

Return `REWORK_REQUIRED` for a concrete barrier.
Return `BLOCKED` when required runtime or assistive tooling is unavailable; state what was and was not checked.
Return `NEEDS_HUMAN_JUDGMENT` only for a true design tradeoff, not to avoid accessibility requirements.
