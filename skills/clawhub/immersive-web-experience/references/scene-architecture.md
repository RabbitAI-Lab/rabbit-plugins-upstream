# Scene Architecture

A scene is a meaningful state of the experience with its own composition, purpose, input mapping, and transition contract. It may span one or several DOM regions.

## Scene contract

For every scene record:

- id, purpose, audience takeaway, and primary action;
- entry state and what arrives from the previous scene;
- ordered beats and their trigger: time, scroll, pointer, click, keyboard, media, or state;
- stage/layer composition and z-order;
- persistent objects and identity across boundaries;
- exit state and properties handed to the next scene;
- pin/scrub duration and progress mapping if relevant;
- mobile, reduced-motion, loading, and failure variants;
- cleanup and ownership boundary.

## Scene map

Represent the experience as nodes and transition edges. Identify the global shell, persistent stage, fixed overlays, normal-flow content, and any WebGL canvas. Avoid making every scene independently mount a new world when continuity is required.

## State model

Separate semantic application state from animation progress. Animation reads state and expresses transitions; it must not become the only record of selected item, navigation location, or content visibility.

## Spatial coherence

Choose axes and meanings. For example, forward/back may mean depth in the story, left/right may mean adjacent chapters, and scale may mean focus. Do not remap these meanings between scenes without teaching the change.
