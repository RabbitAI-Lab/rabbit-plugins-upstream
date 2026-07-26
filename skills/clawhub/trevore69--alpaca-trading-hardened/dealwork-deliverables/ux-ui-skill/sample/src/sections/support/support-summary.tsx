import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import Typography from '@mui/material/Typography';

// ----------------------------------------------------------------------

type SummaryItem = {
  label: string;
  value: string;
};

type Props = {
  items: SummaryItem[];
};

export function SupportSummary({ items }: Props) {
  return (
    <Box
      sx={{
        gap: 3,
        display: 'grid',
        gridTemplateColumns: { xs: 'repeat(2, 1fr)', md: 'repeat(4, 1fr)' },
      }}
    >
      {items.map((item) => (
        <Card key={item.label} sx={{ p: { xs: 2, md: 3 } }}>
          <Typography variant="subtitle2" sx={{ color: 'text.secondary' }}>
            {item.label}
          </Typography>

          <Typography variant="h4" sx={{ mt: 1 }}>
            {item.value}
          </Typography>
        </Card>
      ))}
    </Box>
  );
}
