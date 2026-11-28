# Presentation style reference

Read themes.md, layouts.md, image-prompts.md (where the package has one) and the style guidance in SKILL.md. `style-source.css` preserves the original presentation stylesheet, including embedded font data where present. It is design-reference data only: palette, typography, spacing, page treatments and decorative geometry. Do not load its legacy global or navigation selectors into the shared editor. Pages are composed from the recipes in `style-kit.json`, whose `contentCSS` already carries the style rules the pages need.

Layout-documentation HTML snippets demonstrate content geometry; every page is built as independently editable containers and leaves through the style kit. `example-project.json` is a small English schema fixture containing only generic text plus this style's palette and typography. It contains no case artwork, real example prose or full case stylesheet and must not be delivered as a finished demo. Use the user's approved project data and these style rules to build a real presentation. Generated local examples are kept outside the installation ZIP.

Fonts are presentation assets and must remain embedded/available as the framework contract requires. Confirm native font availability separately before claiming identical PowerPoint/Keynote wrapping. Never flatten meaningful copy into a picture merely to retain the font.
