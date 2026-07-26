import type { UseSetStateReturn } from 'src/hooks/use-set-state';

import { useCallback } from 'react';

import Stack from '@mui/material/Stack';
import MenuItem from '@mui/material/MenuItem';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';

import { Iconify } from 'src/components/iconify';

import { TICKET_PRIORITY_OPTIONS } from './_tickets';

import type { ITicketTableFilters } from './types';

// ----------------------------------------------------------------------

type Props = {
  onResetPage: () => void;
  filters: UseSetStateReturn<ITicketTableFilters>;
};

export function SupportTableToolbar({ filters, onResetPage }: Props) {
  const handleFilterSubject = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      onResetPage();
      filters.setState({ subject: event.target.value });
    },
    [filters, onResetPage]
  );

  const handleFilterPriority = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      onResetPage();
      filters.setState({ priority: event.target.value });
    },
    [filters, onResetPage]
  );

  return (
    <Stack
      spacing={2}
      alignItems={{ xs: 'flex-end', md: 'center' }}
      direction={{ xs: 'column', md: 'row' }}
      sx={{ p: 2.5 }}
    >
      <TextField
        fullWidth
        value={filters.state.subject}
        onChange={handleFilterSubject}
        placeholder="Search tickets or requesters..."
        InputProps={{
          startAdornment: (
            <InputAdornment position="start">
              <Iconify icon="eva:search-fill" sx={{ color: 'text.disabled' }} />
            </InputAdornment>
          ),
        }}
      />

      <TextField
        select
        label="Priority"
        value={filters.state.priority}
        onChange={handleFilterPriority}
        sx={{ width: { xs: 1, md: 200 }, flexShrink: 0 }}
      >
        <MenuItem value="all">All</MenuItem>
        {TICKET_PRIORITY_OPTIONS.map((option) => (
          <MenuItem key={option.value} value={option.value}>
            {option.label}
          </MenuItem>
        ))}
      </TextField>
    </Stack>
  );
}
