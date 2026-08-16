# Figure Reading and Reuse Rubric

Use this rubric for original paper figures, screenshots, and extracted panels.

## Before Interpretation

1. Confirm the figure number and caption.
2. Read the relevant Results and Methods text.
3. Identify the comparison, unit of analysis, sample size, and uncertainty
   display when available.
4. Determine whether the image may be embedded in the intended output.

If reuse rights are unclear, do not add the figure to a public repository.
Link to the source and describe the panel instead, or create an original
teaching diagram that does not copy the publisher's artwork.

## Full Figure Before Panels

For a permitted multi-panel figure:

1. Present the complete figure or a source link first.
2. Explain what question the entire figure addresses.
3. Explain how the panels form one argument.
4. Then inspect individual panels.

This prevents local panel details from being mistaken for the paper's whole
claim.

## Panel Explanation

For each important panel, cover:

- **What is shown?** Experimental condition, model output, anatomy, or data.
- **How do I read it?** Axes, units, color scale, symbols, lines, boxes, labels,
  controls, and uncertainty.
- **Where is the evidence?** Name the visible region or comparison supporting
  the claim.
- **What follows?** State the narrow conclusion justified by the panel.
- **Why does it matter?** Connect the result to the paper's argument.
- **What might be misread?** Identify a tempting but unsupported inference.

Do not jump from “this is Figure 3B” to a conclusion without tracing the
visible evidence.

## Reproducible Crops

When creating crops:

- Record source dimensions and explicit `(left, top, right, bottom)` bounds.
- Preserve panel letters, axes, units, legends, scale bars, and meaningful
  margins.
- Remove neighboring-panel residue or explicitly say what to ignore.
- Store the crop script beside the guide.
- Re-run the script and visually inspect at least one output.

## Evidence Boundaries

Label these separately:

- direct observation or reported measurement;
- statistical comparison;
- author interpretation;
- your teaching analogy;
- unresolved ambiguity or limitation.

A teaching diagram may clarify a mechanism, but it is not new experimental
evidence.
