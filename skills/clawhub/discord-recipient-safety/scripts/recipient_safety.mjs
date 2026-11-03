#!/usr/bin/env node
import fs from 'node:fs';
const block = (reason) => ({ decision: 'BLOCK', reason });
const readJson = (path) => JSON.parse(fs.readFileSync(path, 'utf8'));
const targetFor = (discordUserId) => 'user:' + discordUserId;
const activeMatch = (members, discordUserId) => members.filter((member) => member.discordUserId === discordUserId);
export function validatePreSend(request, roster, pause) {
  if (!request?.requester?.discordUserId || !request?.instruction?.sourceMessageId || !request?.requestedRecipient || request.instruction.exactRecipientName !== request.requestedRecipient || !request?.contentClassification) return block('MISSING_EXPLICIT_RECIPIENT_INSTRUCTION');
  if (!pause || pause.relayPaused !== false) return block('RELAY_PAUSED_OR_UNKNOWN');
  if (!Array.isArray(roster?.members)) return block('INVALID_APPROVED_ROSTER');
  const requesterMatches = activeMatch(roster.members, request.requester.discordUserId);
  if (requesterMatches.length !== 1) return block('REQUESTER_NOT_UNIQUELY_FOUND');
  const requester = requesterMatches[0];
  if (requester.active !== true || requester.approved !== true || requester.canRequestRelay !== true) return block('REQUESTER_INACTIVE_OR_UNAPPROVED');
  const recipientMatches = roster.members.filter((member) => member.canonicalName === request.requestedRecipient);
  if (recipientMatches.length !== 1) return block('RECIPIENT_NOT_UNIQUELY_FOUND');
  const recipient = recipientMatches[0];
  if (recipient.active !== true || recipient.approved !== true || recipient.canReceiveRelay !== true || !/^\d{5,30}$/.test(recipient.discordUserId || '')) return block('RECIPIENT_INACTIVE_OR_UNAPPROVED');
  const exactMessageTarget = targetFor(recipient.discordUserId);
  if (!/^user:\d{5,30}$/.test(request.intendedTarget || '') || request.intendedTarget !== exactMessageTarget) return block('TARGET_MISMATCH');
  return { decision: 'PASS', binding: { requesterDiscordUserId: requester.discordUserId, requesterCanonicalName: requester.canonicalName, requesterInstructionId: request.instruction.sourceMessageId, requestedRecipient: request.requestedRecipient, canonicalRecipient: recipient.canonicalName, discordUserId: recipient.discordUserId, exactMessageTarget, attributionPrefix: 'Requested by ' + requester.canonicalName + ':', contentClassification: request.contentClassification } };
}
export function validateReceipt(binding, delivery) {
  const expected = binding?.binding;
  if (binding?.decision !== 'PASS' || !expected?.attributionPrefix || !delivery?.platformMessageId || !['sent', 'delivered'].includes(delivery?.deliveryResult)) return block('MISSING_DELIVERY_RECEIPT');
  if (delivery.exactMessageTarget !== expected.exactMessageTarget) return block('DELIVERY_TARGET_MISMATCH');
  if (delivery.requesterDiscordUserId !== expected.requesterDiscordUserId) return block('DELIVERY_REQUESTER_MISMATCH');
  if (delivery.attributionPrefix !== expected.attributionPrefix) return block('DELIVERY_ATTRIBUTION_MISMATCH');
  return { decision: 'PASS', receipt: { requestedRecipient: expected.requestedRecipient, canonicalRecipient: expected.canonicalRecipient, targetId: expected.discordUserId, platformMessageId: delivery.platformMessageId, deliveryResult: delivery.deliveryResult } };
}
const arg = (name) => { const index = process.argv.indexOf(name); return index >= 0 ? process.argv[index + 1] : undefined; };
if (process.argv[1] && import.meta.url.endsWith(process.argv[1])) {
  try {
    const command = process.argv[2];
    const result = command === 'pre-send' ? validatePreSend(readJson(arg('--request')), readJson(arg('--roster')), readJson(arg('--pause'))) : command === 'receipt' ? validateReceipt(readJson(arg('--binding')), readJson(arg('--delivery'))) : block('UNKNOWN_COMMAND');
    console.log(JSON.stringify(result));
    process.exitCode = result.decision === 'PASS' ? 0 : 2;
  } catch { console.log(JSON.stringify(block('INVALID_INPUT'))); process.exitCode = 2; }
}