# Scroll Storytelling

Scroll can control progress, reveal sequence, or spatial travel. Choose one dominant interpretation per passage.

## Mapping scroll to story

Define beats at semantic thresholds rather than evenly distributing all changes. Allow dwell time for reading. Pin only while the stage is actively transforming; release as soon as normal reading should resume.

Use scrub for continuous relationships such as camera movement, object assembly, or timeline progress. Use discrete triggers for events that should complete predictably. Avoid scrubbing small UI responses.

## Pacing

Calibrate scroll distance to information density and input device. Long pins can feel trapped on touch devices. Provide visible progress or a clear changing state during extended passages.

## Robustness

- Keep document height stable while assets load.
- Refresh measurements after fonts/media are ready and on meaningful layout changes.
- Test forward, reverse, fast fling, trackpad, wheel, touch, scrollbar drag, resize, and deep-link entry.
- Avoid nested pinned containers and competing smooth-scroll ownership unless the architecture explicitly supports them.

Never hijack native scroll without a specific experiential reason and a complete keyboard/touch/accessibility strategy.
