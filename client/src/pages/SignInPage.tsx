import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { Avatar, Box, Button, Container, CssBaseline, Grid, TextField, Typography } from '@mui/material';
import { Logo } from 'components';
import { Link } from 'react-router-dom';

function SignInPage() {
	return (
		<Container component="main" maxWidth="xs">
			<CssBaseline />
			<Box
				sx={ {
					marginTop: 8,
					display: 'flex',
					flexDirection: 'column',
					alignItems: 'center',
				} }
			>
				<Avatar sx={ { m: 1, bgcolor: 'secondary.main' } }>
					<LockOutlinedIcon />
				</Avatar>
				<Typography component="h1" variant="h5">
					Sign in
				</Typography>
				<Box component="form" onSubmit={ () => { } } noValidate sx={ { mt: 1 } }>
					<TextField
						margin="normal"
						required
						fullWidth
						id="email"
						label="Email Address"
						name="email"
						autoComplete="email"
						autoFocus
					/>
					<TextField
						margin="normal"
						required
						fullWidth
						name="password"
						label="Password"
						type="password"
						id="password"
						autoComplete="current-password"
					/>
					<Button
						type="submit"
						fullWidth
						variant="contained"
						sx={ { mt: 3, mb: 2 } }
					>
						Sign In
					</Button>
					<Grid container>
						<Grid item xs>
							<Link className="text-primary text-sm underline" to=".">
								Forgot password?
							</Link>
						</Grid>
						<Grid item>
							<Link className="text-primary text-sm underline" to="/signup">
								Don't have an account? Sign Up
							</Link>
						</Grid>
					</Grid>
				</Box>
			</Box>
			<Link to='..'>
				<Logo className='mt-8 justify-center' />
			</Link>
		</Container>
	);
}

export default SignInPage;