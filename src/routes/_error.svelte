<script>
	export let status;
	export let error;

	const dev = process.env.NODE_ENV === "development";
</script>

<svelte:head>
	<title>404 | Smiles_Realiza</title>
</svelte:head>

<div class="not-found">
	<img src="/404.svg" alt="" />
</div>

<style>
 	.not-found{
		 height: 100%;
		 width: 100%;
		 display: flex;
		 align-items: center;
		 justify-content: center;
	 }
</style>
