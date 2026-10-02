#!/usr/bin/env node
/** a43.mjs — A1~A3：distillManual 的占位符守卫与 anti_patterns/source 透传（直连，无 spawn）。 */
import * as d from '../code/engine/light/distill.mjs';

const a1 = d.distillManual({ strategy: 'AVOID: x. FIX: <在此填写可执行修法>', signals: ['encoding-error'] });
console.log('A1', (a1.gene === null && /拒绝/.test(String(a1.raw))) ? 1 : 0, String(a1.raw).slice(0, 40));

const a2 = d.distillManual({
	strategy: "FIX: read with encoding='gbk'", signals: ['encoding-error'],
	antiPatterns: ['assume-default-utf8'], source: 'light-manual-guided',
});
console.log('A2', (a2.gene && a2.gene.anti_patterns[0] === 'assume-default-utf8') ? 1 : 0);
console.log('A3', (a2.gene && a2.gene.generation_meta.source === 'light-manual-guided') ? 1 : 0);
