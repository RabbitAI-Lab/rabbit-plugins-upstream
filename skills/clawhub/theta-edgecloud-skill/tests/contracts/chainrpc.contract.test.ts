import assert from 'node:assert/strict';
import test from 'node:test';
import { listThetaRuntimeCommands } from '../../dist/index.js';

test('wallet, rewards and local chain RPC are not exposed by the cloud runtime', () => {
  assert.equal(listThetaRuntimeCommands().some(c=>/wallet|reward|rpc/i.test(c)),false);
});
