import { fSub } from 'src/utils/format-time';

import { _mock } from 'src/_mock';

import type { ITicketItem, TicketStatus, TicketPriority } from './types';

// ----------------------------------------------------------------------

export const TICKET_STATUS_OPTIONS = [
  { value: 'open', label: 'Open' },
  { value: 'in_progress', label: 'In progress' },
  { value: 'resolved', label: 'Resolved' },
  { value: 'closed', label: 'Closed' },
];

export const TICKET_PRIORITY_OPTIONS = [
  { value: 'low', label: 'Low' },
  { value: 'medium', label: 'Medium' },
  { value: 'high', label: 'High' },
  { value: 'urgent', label: 'Urgent' },
];

type TicketSeed = {
  subject: string;
  status: TicketStatus;
  priority: TicketPriority;
  /** Hours since the ticket was last updated. Kept above one hour so the
   *  relative timestamp renders identically on the server and the client. */
  hoursAgo: number;
};

const TICKET_SEED: TicketSeed[] = [
  { subject: 'Checkout fails on saved card', status: 'open', priority: 'urgent', hoursAgo: 3 },
  {
    subject: 'Cannot export monthly invoice',
    status: 'in_progress',
    priority: 'medium',
    hoursAgo: 7,
  },
  { subject: 'Two-factor code never arrives', status: 'open', priority: 'high', hoursAgo: 11 },
  {
    subject: 'Team seat count is wrong after upgrade',
    status: 'resolved',
    priority: 'low',
    hoursAgo: 26,
  },
  { subject: 'Webhook retries stopped overnight', status: 'open', priority: 'high', hoursAgo: 32 },
  {
    subject: 'Password reset link expired instantly',
    status: 'closed',
    priority: 'medium',
    hoursAgo: 50,
  },
  {
    subject: 'Duplicate charge on annual renewal',
    status: 'open',
    priority: 'urgent',
    hoursAgo: 74,
  },
  {
    subject: 'Dashboard slow on large accounts',
    status: 'in_progress',
    priority: 'low',
    hoursAgo: 96,
  },
  {
    subject: 'API returns 403 after key rotation',
    status: 'resolved',
    priority: 'medium',
    hoursAgo: 120,
  },
  { subject: 'Sub-account cannot access reports', status: 'open', priority: 'high', hoursAgo: 150 },
  {
    subject: 'Email notifications going to spam',
    status: 'closed',
    priority: 'low',
    hoursAgo: 190,
  },
  {
    subject: 'CSV import drops the last row',
    status: 'in_progress',
    priority: 'medium',
    hoursAgo: 240,
  },
];

export const _tickets: ITicketItem[] = TICKET_SEED.map((seed, index) => ({
  id: _mock.id(index),
  reference: `TCK-${2140 + index}`,
  subject: seed.subject,
  requesterName: _mock.fullName(index),
  requesterEmail: _mock.email(index),
  requesterAvatar: _mock.image.avatar(index),
  priority: seed.priority,
  status: seed.status,
  updatedAt: fSub({ hours: seed.hoursAgo }),
}));
