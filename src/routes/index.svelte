<script>
	import Search from '../components/Search.svelte'
</script>

<svelte:head>
	<title>Home | Smiles Realiza </title>
</svelte:head>

<div class="home-container">
	<div class="content">
		<Search />
	</div>
	<footer>
		<h1>
			CONHEÇA MAIS SOBRE O PROGRAMA
			<i class="fas fa-chevron-down"></i>
		</h1>

	</footer>
</div>

<style>
	.home-container{
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.content{
		width: 100%;
		height: 60%;
		margin-bottom: 5rem;
	}
	footer h1{
		height: 60%;
		color: var(--main-color);
		text-align: center;
		font-size: 3rem;
		height: 100%;
		display: flex;
		flex-direction: column;
	}
</style>
