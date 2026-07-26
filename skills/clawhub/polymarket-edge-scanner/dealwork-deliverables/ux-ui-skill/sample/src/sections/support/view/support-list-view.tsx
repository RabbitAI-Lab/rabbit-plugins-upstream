'use client';

import { useState, useCallback } from 'react';

import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Card from '@mui/material/Card';
import Table from '@mui/material/Table';
import Button from '@mui/material/Button';
import TableBody from '@mui/material/TableBody';

import { paths } from 'src/routes/paths';

import { useBoolean } from 'src/hooks/use-boolean';
import { useSetState } from 'src/hooks/use-set-state';

import { varAlpha } from 'src/theme/styles';
import { DashboardContent } from 'src/layouts/dashboard';

import { Label } from 'src/components/label';
import { toast } from 'src/components/snackbar';
import { Iconify } from 'src/components/iconify';
import { Scrollbar } from 'src/components/scrollbar';
import { ConfirmDialog } from 'src/components/custom-dialog';
import { CustomBreadcrumbs } from 'src/components/custom-breadcrumbs';
import {
  useTable,
  emptyRows,
  rowInPage,
  TableNoData,
  getComparator,
  TableEmptyRows,
  TableHeadCustom,
  TablePaginationCustom,
} from 'src/components/table';

import { SupportSummary } from '../support-summary';
import { SupportTableRow } from '../support-table-row';
import { _tickets, TICKET_STATUS_OPTIONS } from '../_tickets';
import { SupportTableToolbar } from '../support-table-toolbar';
import { SupportNewTicketDialog } from '../support-new-ticket-dialog';

import type { NewTicketValues } from '../support-new-ticket-dialog';
import type { ITicketItem, TicketStatus, ITicketTableFilters } from '../types';

// ----------------------------------------------------------------------

const STATUS_OPTIONS = [{ value: 'all', label: 'All' }, ...TICKET_STATUS_OPTIONS];

const TABLE_HEAD = [
  { id: 'subject', label: 'Ticket' },
  { id: 'requesterName', label: 'Requester', width: 260 },
  { id: 'priority', label: 'Priority', width: 120 },
  { id: 'status', label: 'Status', width: 140 },
  { id: 'updatedAt', label: 'Updated', width: 160 },
  { id: '', width: 68 },
];

const STATUS_TAB_COLOR = {
  open: 'info',
  in_progress: 'warning',
  resolved: 'success',
  closed: 'default',
} as const;

// ----------------------------------------------------------------------

export function SupportListView() {
  const table = useTable({ defaultOrderBy: 'updatedAt', defaultOrder: 'desc' });

  const newTicket = useBoolean();

  const confirm = useBoolean();

  const [tableData, setTableData] = useState<ITicketItem[]>(_tickets);

  const [pendingDeleteId, setPendingDeleteId] = useState<string | null>(null);

  const filters = useSetState<ITicketTableFilters>({
    subject: '',
    status: 'all',
    priority: 'all',
  });

  const dataFiltered = applyFilter({
    inputData: tableData,
    comparator: getComparator(table.order, table.orderBy),
    filters: filters.state,
  });

  const dataInPage = rowInPage(dataFiltered, table.page, table.rowsPerPage);

  const notFound = !dataFiltered.length;

  const countByStatus = (status: string) =>
    status === 'all'
      ? tableData.length
      : tableData.filter((ticket) => ticket.status === status).length;

  const summaryItems = [
    { label: 'Open', value: `${countByStatus('open')}` },
    { label: 'In progress', value: `${countByStatus('in_progress')}` },
    { label: 'Resolved this week', value: `${countByStatus('resolved')}` },
    { label: 'Median first response', value: '1h 42m' },
  ];

  const handleFilterStatus = useCallback(
    (event: React.SyntheticEvent, newValue: string) => {
      table.onResetPage();
      filters.setState({ status: newValue });
    },
    [filters, table]
  );

  const handleCreateTicket = useCallback(
    (values: NewTicketValues) => {
      const created: ITicketItem = {
        id: `local-${Date.now()}`,
        reference: `TCK-${2140 + tableData.length}`,
        subject: values.subject,
        requesterName: values.requesterEmail.split('@')[0],
        requesterEmail: values.requesterEmail,
        requesterAvatar: '',
        priority: values.priority,
        status: 'open',
        updatedAt: new Date(),
      };

      setTableData((prev) => [created, ...prev]);
      newTicket.onFalse();
      toast.success('Ticket created');
    },
    [newTicket, tableData.length]
  );

  const handleAssignRow = useCallback((id: string) => {
    setTableData((prev) =>
      prev.map((ticket) =>
        ticket.id === id ? { ...ticket, status: 'in_progress' as TicketStatus } : ticket
      )
    );
    toast.success('Ticket assigned to you');
  }, []);

  const handleResolveRow = useCallback((id: string) => {
    setTableData((prev) =>
      prev.map((ticket) =>
        ticket.id === id ? { ...ticket, status: 'resolved' as TicketStatus } : ticket
      )
    );
    toast.success('Ticket marked as resolved');
  }, []);

  const handleRequestDelete = useCallback(
    (id: string) => {
      setPendingDeleteId(id);
      confirm.onTrue();
    },
    [confirm]
  );

  const handleConfirmDelete = useCallback(() => {
    if (pendingDeleteId) {
      setTableData((prev) => prev.filter((ticket) => ticket.id !== pendingDeleteId));
      table.onUpdatePageDeleteRow(dataInPage.length);
      toast.success('Ticket deleted');
    }
    setPendingDeleteId(null);
    confirm.onFalse();
  }, [confirm, dataInPage.length, pendingDeleteId, table]);

  return (
    <>
      <DashboardContent>
        <CustomBreadcrumbs
          heading="Support tickets"
          links={[{ name: 'Dashboard', href: paths.dashboard.root }, { name: 'Support tickets' }]}
          action={
            <Button
              variant="contained"
              startIcon={<Iconify icon="mingcute:add-line" />}
              onClick={newTicket.onTrue}
            >
              New ticket
            </Button>
          }
          sx={{ mb: { xs: 3, md: 5 } }}
        />

        <Box sx={{ mb: { xs: 3, md: 5 } }}>
          <SupportSummary items={summaryItems} />
        </Box>

        <Card>
          <Tabs
            value={filters.state.status}
            onChange={handleFilterStatus}
            sx={{
              px: 2.5,
              boxShadow: (theme) =>
                `inset 0 -2px 0 0 ${varAlpha(theme.vars.palette.grey['500Channel'], 0.08)}`,
            }}
          >
            {STATUS_OPTIONS.map((tab) => (
              <Tab
                key={tab.value}
                iconPosition="end"
                value={tab.value}
                label={tab.label}
                icon={
                  <Label
                    variant={
                      ((tab.value === 'all' || tab.value === filters.state.status) && 'filled') ||
                      'soft'
                    }
                    color={
                      STATUS_TAB_COLOR[tab.value as keyof typeof STATUS_TAB_COLOR] ?? 'default'
                    }
                  >
                    {countByStatus(tab.value)}
                  </Label>
                }
              />
            ))}
          </Tabs>

          <SupportTableToolbar filters={filters} onResetPage={table.onResetPage} />

          <Box sx={{ position: 'relative' }}>
            <Scrollbar sx={{ minHeight: 444 }}>
              <Table size={table.dense ? 'small' : 'medium'} sx={{ minWidth: 960 }}>
                <TableHeadCustom
                  order={table.order}
                  orderBy={table.orderBy}
                  headLabel={TABLE_HEAD}
                  rowCount={dataFiltered.length}
                  onSort={table.onSort}
                />

                <TableBody>
                  {dataInPage.map((row) => (
                    <SupportTableRow
                      key={row.id}
                      row={row}
                      onViewRow={() => toast.info(`Opening ${row.reference}`)}
                      onAssignRow={() => handleAssignRow(row.id)}
                      onResolveRow={() => handleResolveRow(row.id)}
                      onDeleteRow={() => handleRequestDelete(row.id)}
                    />
                  ))}

                  <TableEmptyRows
                    height={table.dense ? 56 : 76}
                    emptyRows={emptyRows(table.page, table.rowsPerPage, dataFiltered.length)}
                  />

                  <TableNoData notFound={notFound} />
                </TableBody>
              </Table>
            </Scrollbar>
          </Box>

          <TablePaginationCustom
            page={table.page}
            dense={table.dense}
            count={dataFiltered.length}
            rowsPerPage={table.rowsPerPage}
            onPageChange={table.onChangePage}
            onChangeDense={table.onChangeDense}
            onRowsPerPageChange={table.onChangeRowsPerPage}
          />
        </Card>
      </DashboardContent>

      <SupportNewTicketDialog
        open={newTicket.value}
        onClose={newTicket.onFalse}
        onCreate={handleCreateTicket}
      />

      <ConfirmDialog
        open={confirm.value}
        onClose={confirm.onFalse}
        title="Delete ticket"
        content="This ticket will be permanently removed. This cannot be undone."
        action={
          <Button variant="contained" color="error" onClick={handleConfirmDelete}>
            Delete
          </Button>
        }
      />
    </>
  );
}

// ----------------------------------------------------------------------

type ApplyFilterProps = {
  inputData: ITicketItem[];
  filters: ITicketTableFilters;
  comparator: (a: any, b: any) => number;
};

function applyFilter({ inputData, comparator, filters }: ApplyFilterProps) {
  const { subject, status, priority } = filters;

  const stabilized = inputData.map((el, index) => [el, index] as const);

  stabilized.sort((a, b) => {
    const order = comparator(a[0], b[0]);
    if (order !== 0) return order;
    return a[1] - b[1];
  });

  let data = stabilized.map((el) => el[0]);

  if (subject) {
    const query = subject.toLowerCase();
    data = data.filter(
      (ticket) =>
        ticket.subject.toLowerCase().includes(query) ||
        ticket.reference.toLowerCase().includes(query) ||
        ticket.requesterName.toLowerCase().includes(query) ||
        ticket.requesterEmail.toLowerCase().includes(query)
    );
  }

  if (status !== 'all') {
    data = data.filter((ticket) => ticket.status === status);
  }

  if (priority !== 'all') {
    data = data.filter((ticket) => ticket.priority === priority);
  }

  return data;
}
