import React, { useState, useEffect } from "react";
import {
	FormControl,
	TextField,
	Button,
	Typography,
	makeStyles,
	CircularProgress
} from "@material-ui/core";
import { useHistory, Link } from "react-router-dom";

// import axios from "axios";
import { postData } from "../../helpers";
import { useAuthValue } from "../../context";

import "../../styles/LoginForm.css";

const useStyles = makeStyles(theme => ({
	formControl: {
		margin: theme.spacing(1)
	},
	button: {
		margin: theme.spacing(1)
	}
}));

const LoginForm = () => {
	const { setAuth, setUsername } = useAuthValue();

	const [usernameField, setUsernameField] = useState("");
	const [password, setPassword] = useState("");
	const [loggingIn, setLoggingIn] = useState(false);

	const classes = useStyles();
	const history = useHistory();

	useEffect(() => {
		document.title = "Login";
		return () => (document.title = "FlightApp");
	}, []);

	const handleLogin = () => {
		setLoggingIn(true);
		const data = { username: usernameField, password };

		const response = postData("api/token/", data);
		// const response = axios.post(
		// `${process.env.REACT_APP_API_URL}api/token/`,
		// data
		// );
		response.then(res => {
			localStorage.setItem("access", res.data.access);
			localStorage.setItem("refresh", res.data.refresh);
			const today = new Date();

			localStorage.setItem(
				"expirationDate",
				today.setDate(today.getDate() + 28)
			);
			setAuth(true);
			setUsername(usernameField);
			setLoggingIn(false);
			history.push("/countries");
		});

		response.catch(err => {
			console.log(err);
			setLoggingIn(false);
		});
	};

	let loginButton;
	if (loggingIn) {
		loginButton = (
			<Button variant="contained" id="login-submit-btn" disabled>
				<CircularProgress />
			</Button>
		);
	} else {
		loginButton = (
			<Button variant="contained" id="login-submit-btn" onClick={handleLogin}>
				Login
			</Button>
		);
	}

	return (
		<div id="form-container">
			<Typography style={{ marginTop: 10 }}>Login</Typography>

			<FormControl className={classes.formControl}>
				<TextField
					variant="outlined"
					label="Username"
					value={usernameField}
					onChange={event => setUsernameField(event.target.value)}
				/>
			</FormControl>

			<FormControl className={classes.formControl}>
				<TextField
					variant="outlined"
					label="Password"
					type="password"
					value={password}
					onChange={event => setPassword(event.target.value)}
				/>
			</FormControl>

			<Link
				className="link"
				to="/registration"
				style={{ color: "gray", marginBottom: 10 }}
			>
				Don't have an account? Click Here
			</Link>

			{loginButton}
		</div>
	);
};

export default LoginForm;
