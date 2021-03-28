<script>
	export let segment;
</script>

<nav>
	<ul>
		<div class="icon">
			<a href=".">
				<img src="logo.svg" alt="" />
			</a>
		</div>
		<div class="options">
			<li>
				<a href="ajuda">ajuda </a>
			</li>
			<li>
				<a href="registro">cadastre-se </a>
			</li>
			<li>
				<a
					class="login"
					href="login">entrar</a
				>
			</li>
		</div>
	</ul>
</nav>

<style>
	nav {
		font-weight: 400;
		width: 100%;
		background-color: var(--main-color);
		padding-left: 4rem;
		padding-right: 4rem;
	}

	ul {
		margin: 0;
		display: flex;
		align-items: center;
		justify-content: space-between;
		height: 5rem;
	}

	li {
		display: block;
		float: left;
	}

	a {
		text-decoration: none;
		margin-left: 1rem;
		padding-top: 1rem;
		padding-bottom: 1rem;
		display: block;
		color: var(--white);
		text-transform: capitalize;
		transition: ease 0.2s;
		font-weight: 600;
	}

	a:hover {
		filter: opacity(0.7);
	}

	.icon a > img {
		width: 5rem;
	}
	.icon a {
		transition: ease 0.2s;
	}
	.icon:hover a {
		filter: opacity(1);
		transform: scale(1.2);
	}

	.login {
		border: solid 3px var(--white);
		padding-right: 2rem;
		padding-left: 2rem;
		font-weight: 900;
		margin-left: 1rem;
		transition: ease 0.2s;
	}
	.login:hover {
		color: var(--main-color);
		background-color: var(--white);
		filter: opacity(1);
	}
</style>
