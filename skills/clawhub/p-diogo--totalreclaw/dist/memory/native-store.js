/**
 * Build the truthful `memory_save` store fn. Return semantics (the whole point
 * of #499 — never report success on a non-persist):
 * - init throws            → `{ ok:false, stored:0, error:'setup incomplete: …' }`
 * - not paired             → `{ ok:false, stored:0, error:'not paired — …' }`
 * - storeFacts throws      → `{ ok:false, stored:0, error:<msg> }`
 * - storeFacts returns 0   → `{ ok:true,  stored:0 }` (dedup/skip — agent says
 *                            "duplicate, not stored", never "Saved")
 * - storeFacts returns >=1 → `{ ok:true,  stored:n }`
 */
export function buildNativeStore(ctx) {
    return async (input) => {
        try {
            await ctx.ensureInit();
        }
        catch (e) {
            const msg = e instanceof Error ? e.message : String(e);
            return { ok: false, stored: 0, error: `setup incomplete: ${msg}` };
        }
        if (!ctx.isPaired()) {
            return { ok: false, stored: 0, error: 'not paired — complete TotalReclaw setup first' };
        }
        const fact = {
            text: input.text,
            type: input.type ?? 'claim',
            importance: input.importance ?? 8,
            action: 'ADD',
            confidence: 1.0,
            source: 'user',
            ...(input.entities ? { entities: input.entities } : {}),
            ...(input.scope ? { scope: input.scope } : {}),
            ...(input.reasoning ? { reasoning: input.reasoning } : {}),
        };
        try {
            const stored = await ctx.storeFacts([fact]);
            return { ok: true, stored };
        }
        catch (e) {
            const msg = e instanceof Error ? e.message : String(e);
            return { ok: false, stored: 0, error: msg };
        }
    };
}
