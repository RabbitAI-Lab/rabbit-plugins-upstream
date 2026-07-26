import Stack from '@mui/material/Stack';
import Avatar from '@mui/material/Avatar';
import Divider from '@mui/material/Divider';
import MenuList from '@mui/material/MenuList';
import MenuItem from '@mui/material/MenuItem';
import TableRow from '@mui/material/TableRow';
import TableCell from '@mui/material/TableCell';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import ListItemText from '@mui/material/ListItemText';

import { fToNow } from 'src/utils/format-time';

import { Label } from 'src/components/label';
import { Iconify } from 'src/components/iconify';
import { usePopover, CustomPopover } from 'src/components/custom-popover';

import type { ITicketItem } from './types';

// ----------------------------------------------------------------------

const STATUS_COLOR = {
  open: 'info',
  in_progress: 'warning',
  resolved: 'success',
  closed: 'default',
} as const;

const STATUS_LABEL = {
  open: 'Open',
  in_progress: 'In progress',
  resolved: 'Resolved',
  closed: 'Closed',
} as const;

const PRIORITY_COLOR = {
  low: 'default',
  medium: 'info',
  high: 'warning',
  urgent: 'error',
} as const;

type Props = {
  row: ITicketItem;
  onViewRow: () => void;
  onAssignRow: () => void;
  onResolveRow: () => void;
  onDeleteRow: () => void;
};

export function SupportTableRow({ row, onViewRow, onAssignRow, onResolveRow, onDeleteRow }: Props) {
  const popover = usePopover();

  const handleMenuAction = (action: () => void) => () => {
    popover.onClose();
    action();
  };

  return (
    <>
      <TableRow hover tabIndex={-1}>
        <TableCell>
          <ListItemText
            primary={row.subject}
            secondary={row.reference}
            primaryTypographyProps={{ typography: 'body2', noWrap: true }}
            secondaryTypographyProps={{ component: 'span', typography: 'caption' }}
          />
        </TableCell>

        <TableCell>
          <Stack direction="row" alignItems="center" spacing={2}>
            <Avatar alt={row.requesterName} src={row.requesterAvatar || undefined}>
              {row.requesterName.charAt(0).toUpperCase()}
            </Avatar>
            <ListItemText
              primary={row.requesterName}
              secondary={row.requesterEmail}
              primaryTypographyProps={{ typography: 'body2' }}
              secondaryTypographyProps={{ component: 'span', typography: 'caption' }}
            />
          </Stack>
        </TableCell>

        <TableCell>
          <Label variant="soft" color={PRIORITY_COLOR[row.priority]}>
            {row.priority}
          </Label>
        </TableCell>

        <TableCell>
          <Label variant="soft" color={STATUS_COLOR[row.status]}>
            {STATUS_LABEL[row.status]}
          </Label>
        </TableCell>

        <TableCell>
          <Typography variant="body2" sx={{ color: 'text.secondary' }} noWrap>
            {fToNow(row.updatedAt)}
          </Typography>
        </TableCell>

        <TableCell align="right" sx={{ px: 1 }}>
          <IconButton
            aria-label="Ticket actions"
            color={popover.open ? 'inherit' : 'default'}
            onClick={popover.onOpen}
          >
            <Iconify icon="eva:more-vertical-fill" />
          </IconButton>
        </TableCell>
      </TableRow>

      <CustomPopover
        open={popover.open}
        anchorEl={popover.anchorEl}
        onClose={popover.onClose}
        slotProps={{ arrow: { placement: 'right-top' } }}
      >
        <MenuList>
          <MenuItem onClick={handleMenuAction(onViewRow)}>
            <Iconify icon="solar:eye-bold" />
            View details
          </MenuItem>

          <MenuItem onClick={handleMenuAction(onAssignRow)}>
            <Iconify icon="solar:user-plus-bold" />
            Assign to me
          </MenuItem>

          <MenuItem
            onClick={handleMenuAction(onResolveRow)}
            disabled={row.status === 'resolved' || row.status === 'closed'}
          >
            <Iconify icon="solar:check-circle-bold" />
            Mark as resolved
          </MenuItem>

          <Divider sx={{ borderStyle: 'dashed' }} />

          <MenuItem onClick={handleMenuAction(onDeleteRow)} sx={{ color: 'error.main' }}>
            <Iconify icon="solar:trash-bin-trash-bold" />
            Delete
          </MenuItem>
        </MenuList>
      </CustomPopover>
    </>
  );
}
