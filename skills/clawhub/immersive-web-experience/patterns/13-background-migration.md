# Background Migration

Keep the environmental field continuous while foreground content changes.

**Use when:** chapters share one world but shift mood, location, or focus.

**Build:** place background ownership above individual scene components; interpolate position, color, crop, light, or texture across boundaries; keep foreground transitions quieter. Separate background state from content state.

**Continuity:** the field is the persistent object.

**Avoid:** repainting large layers unnecessarily, low-contrast intermediate states, and background motion competing with reading. Reduced motion changes the field discretely at scene boundaries.
