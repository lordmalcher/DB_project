import React, { useState, useEffect } from "react";
import { Table, TableRow, TableCell, TableBody } from "@material-ui/core";

import { fetchData, listSort } from "../helpers";
import { TableToolbar, TableHeader, TableActions } from "./table";

const AirplanesList = () => {
	const [airplanes, setAirplanes] = useState([]);
	const [ogAirplanes, setOgAirplanes] = useState([]);
	const [registrationFilter, setRegistrationFilter] = useState("");
	const [order, setOrder] = useState("desc");
	const [orderBy, setOrderBy] = useState("registration");
	const [edited, setEdited] = useState(false);

	useEffect(() => {
		document.title = "Airplanes List";
	});

	useEffect(() => {
		const response = fetchData("api/airplanes/");
		response.then(res => {
			setAirplanes(res.data);
			setOgAirplanes(res.data);
			setEdited(false);
		});
	}, [edited]);

	useEffect(() => {
		if (ogAirplanes.length > 0) {
			setAirplanes(
				ogAirplanes.filter(row => {
					return row.registration
						.toString()
						.toLowerCase()
						.startsWith(registrationFilter.toLowerCase());
				})
			);
		}
	}, [registrationFilter, ogAirplanes]);

	useEffect(() => {
		if (airplanes.length > 0) {
			setAirplanes(listSort(airplanes, orderBy, order));
		}
	}, [order, orderBy, airplanes]);

	const airplanesTableRows = airplanes.map(airplane => (
		<TableRow key={airplane.id}>
			<TableCell>{airplane.registration}</TableCell>
			<TableCell align="right">{airplane.produced}</TableCell>
			<TableCell align="right">{airplane.airplane_model}</TableCell>
			<TableActions
				editLink={`/airplanes/${airplane.id}/edit`}
				setEdited={setEdited}
				url="api/airplanes"
				itemID={airplane.id}
			/>
		</TableRow>
	));

	const filters = [
		{
			label: "Registration",
			name: "registration",
			value: registrationFilter,
			onChange: setRegistrationFilter
		}
	];

	const headers = [
		{ align: "inherit", name: "Registration" },
		{ align: "right", name: "Produced" },
		{ align: "right", name: "Airplane Model" }
	];

	const handleOrder = name => {
		if (orderBy === name) {
			setOrder(order === "desc" ? "asc" : "desc");
		} else {
			setOrder("desc");
			setOrderBy(name);
		}
	};

	return (
		<div>
			<TableToolbar
				tableTitle="Airplanes"
				addLink="/airplanes/add-airplane"
				filters={filters}
			/>
			<Table>
				<TableHeader
					headers={headers}
					orderBy={orderBy}
					handleOrder={handleOrder}
					order={order}
				/>

				<TableBody>{airplanesTableRows}</TableBody>
			</Table>
		</div>
	);
};

export default AirplanesList;
