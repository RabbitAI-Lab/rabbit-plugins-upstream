import assert from 'node:assert/strict';
import { validatePreSend, validateReceipt } from './recipient_safety.mjs';
const roster = { members: [
  { canonicalName: 'Requester', discordUserId: '111111111111111111', active: true, approved: true, canRequestRelay: true, canReceiveRelay: true },
  { canonicalName: 'Recipient', discordUserId: '222222222222222222', active: true, approved: true, canRequestRelay: true, canReceiveRelay: true },
  { canonicalName: 'Inactive', discordUserId: '333333333333333333', active: false, approved: true, canRequestRelay: true, canReceiveRelay: true }
] };
const request = { requester: { discordUserId: '111111111111111111' }, instruction: { sourceMessageId: 'request-message-id', exactRecipientName: 'Recipient' }, requestedRecipient: 'Recipient', intendedTarget: 'user:222222222222222222', contentClassification: 'confidential' };
const pass = validatePreSend(request, roster, { relayPaused: false });
const delivery = { platformMessageId: 'platform-message-id', deliveryResult: 'sent', exactMessageTarget: 'user:222222222222222222', requesterDiscordUserId: '111111111111111111', attributionPrefix: 'Requested by Requester:' };
assert.equal(pass.decision, 'PASS');
assert.equal(pass.binding.attributionPrefix, 'Requested by Requester:');
assert.equal(validateReceipt(pass, delivery).decision, 'PASS');
assert.equal(validatePreSend({ ...request, intendedTarget: 'user:111111111111111111' }, roster, { relayPaused: false }).decision, 'BLOCK');
assert.equal(validateReceipt(pass, { ...delivery, exactMessageTarget: 'user:111111111111111111' }).decision, 'BLOCK');
assert.equal(validateReceipt(pass, { ...delivery, attributionPrefix: 'Requested by SomeoneElse:' }).decision, 'BLOCK');
assert.equal(validatePreSend({ ...request, requestedRecipient: 'Duplicate', instruction: { sourceMessageId: 'request-message-id', exactRecipientName: 'Duplicate' } }, { members: [...roster.members, { canonicalName: 'Duplicate', discordUserId: '444444444444444444', active: true, approved: true, canRequestRelay: true, canReceiveRelay: true }, { canonicalName: 'Duplicate', discordUserId: '555555555555555555', active: true, approved: true, canRequestRelay: true, canReceiveRelay: true }] }, { relayPaused: false }).decision, 'BLOCK');
assert.equal(validatePreSend({ ...request, requestedRecipient: 'Inactive', instruction: { sourceMessageId: 'request-message-id', exactRecipientName: 'Inactive' }, intendedTarget: 'user:333333333333333333' }, roster, { relayPaused: false }).decision, 'BLOCK');
assert.equal(validatePreSend({ ...request, requester: { discordUserId: '999999999999999999' } }, roster, { relayPaused: false }).decision, 'BLOCK');
assert.equal(validateReceipt(pass, {}).decision, 'BLOCK');
assert.equal(validatePreSend(request, roster, { relayPaused: true }).decision, 'BLOCK');
console.log('PASS 10/10 recipient-safety cases');