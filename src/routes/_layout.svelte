<script>
	import Nav from "../components/Nav.svelte";
	import TopBar from "../components/TopBar.svelte";

	let items = [
		"buscar voos",
		"viajar",
		"clube smiles",
		"promoções",
		"dicas de acúmulo e resgate",
		"cartão de crédito GOL smiles",
		"shopping smiles",
		"dicas smiles",
		"+Smiles",
	];

	export let segment;
</script>

<div class="container">
	<div>
		<TopBar {segment} />
		<Nav {items} />
	</div>

	<main>
		<div>
			<slot />
		</div>
	</main>
</div>

<style>
	.container{
		height: 100vh;
		width: 100vw;
		padding: 0;
		overflow-y: auto;
		overflow-x: hidden;
		display: flex;
		flex-direction: column;
		position: relative;
		
	}
	.container main{
		background-color: var(--beige);
		height: 100%;
		padding-left: 4rem;
		padding-right: 4rem;
	}
	main > div{
		height: 100%;
	}
</style>
