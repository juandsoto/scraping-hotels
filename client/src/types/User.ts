interface User {
	user_id: number;
	first_name: string;
	last_name: string;
	email: string;
	role: 'user' | 'admin';
	state: boolean;
}

export default User;