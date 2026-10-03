#!/usr/bin/env node
/** d43.mjs — D4：store.approvedAssetIds 的审核语义（last-write-wins）行为测试。
 *  用法：EVO_STORE_DIR=<storeI> node d43.mjs
 *  断言：approved 后被 quarantine 的资产不得再出现在「可注入」集合中。 */
import { approvedAssetIds } from '../code/engine/light/store.mjs';

const set = approvedAssetIds();
const kept = set.has('sha256:gene_test_kept');
const revoked = set.has('sha256:gene_test_revoked');
console.log('D4', (kept && !revoked) ? 1 : 0, `approved=[${[...set].join(',')}]`);
