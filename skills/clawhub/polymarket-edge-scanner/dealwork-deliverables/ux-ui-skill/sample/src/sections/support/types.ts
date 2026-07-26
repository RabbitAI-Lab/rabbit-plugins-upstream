export type TicketStatus = 'open' | 'in_progress' | 'resolved' | 'closed';

export type TicketPriority = 'low' | 'medium' | 'high' | 'urgent';

export type ITicketItem = {
  id: string;
  reference: string;
  subject: string;
  requesterName: string;
  requesterEmail: string;
  requesterAvatar: string;
  priority: TicketPriority;
  status: TicketStatus;
  updatedAt: Date | string | number;
};

export type ITicketTableFilters = {
  subject: string;
  status: string;
  priority: string;
};
