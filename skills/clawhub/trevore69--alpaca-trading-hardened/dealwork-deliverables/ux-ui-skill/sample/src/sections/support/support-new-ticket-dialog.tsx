import { useRef, useState, useCallback } from 'react';

import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import MenuItem from '@mui/material/MenuItem';
import TextField from '@mui/material/TextField';
import DialogTitle from '@mui/material/DialogTitle';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';

import { TICKET_PRIORITY_OPTIONS } from './_tickets';

import type { TicketPriority } from './types';

// ----------------------------------------------------------------------

export type NewTicketValues = {
  subject: string;
  requesterEmail: string;
  priority: TicketPriority;
  description: string;
};

const DEFAULT_VALUES: NewTicketValues = {
  subject: '',
  requesterEmail: '',
  priority: 'medium',
  description: '',
};

type Props = {
  open: boolean;
  onClose: () => void;
  onCreate: (values: NewTicketValues) => void;
};

export function SupportNewTicketDialog({ open, onClose, onCreate }: Props) {
  const [values, setValues] = useState<NewTicketValues>(DEFAULT_VALUES);

  const subjectRef = useRef<HTMLInputElement>(null);

  const handleChange = useCallback(
    (field: keyof NewTicketValues) => (event: React.ChangeEvent<HTMLInputElement>) => {
      setValues((prev) => ({ ...prev, [field]: event.target.value }));
    },
    []
  );

  const handleClose = useCallback(() => {
    setValues(DEFAULT_VALUES);
    onClose();
  }, [onClose]);

  const handleCreate = useCallback(() => {
    onCreate(values);
    setValues(DEFAULT_VALUES);
  }, [onCreate, values]);

  const isValid = values.subject.trim() !== '' && values.requesterEmail.trim() !== '';

  return (
    <Dialog
      fullWidth
      maxWidth="sm"
      open={open}
      onClose={handleClose}
      TransitionProps={{ onEntered: () => subjectRef.current?.focus() }}
    >
      <DialogTitle sx={{ pb: 2 }}>New ticket</DialogTitle>

      <DialogContent sx={{ typography: 'body2' }}>
        <Stack spacing={3} sx={{ pt: 1 }}>
          <TextField
            fullWidth
            label="Subject"
            inputRef={subjectRef}
            value={values.subject}
            onChange={handleChange('subject')}
          />

          <TextField
            fullWidth
            label="Requester email"
            value={values.requesterEmail}
            onChange={handleChange('requesterEmail')}
          />

          <TextField
            select
            fullWidth
            label="Priority"
            value={values.priority}
            onChange={handleChange('priority')}
          >
            {TICKET_PRIORITY_OPTIONS.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </TextField>

          <TextField
            fullWidth
            multiline
            rows={3}
            label="Description"
            value={values.description}
            onChange={handleChange('description')}
          />
        </Stack>
      </DialogContent>

      <DialogActions>
        <Button variant="outlined" color="inherit" onClick={handleClose}>
          Cancel
        </Button>

        <Button variant="contained" disabled={!isValid} onClick={handleCreate}>
          Create ticket
        </Button>
      </DialogActions>
    </Dialog>
  );
}
