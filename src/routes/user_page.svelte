<script>
    import CardUserProfile from '../components/CardUserProfile.svelte'
    import {scheduledTrips} from '../stores.js'

</script>

<svelte:head>
	<title>Perfil | Smiles_Realiza </title>
</svelte:head>
<div class="user-page-container">
    <div class="user-greeting">
        <div class="usr-img"></div>
        <h2>Bem vindo(a), <b>Usuário</b></h2>
    </div>
    <div class="current-cards">
        <p>Aqui estão seus pacotes:</p>
        <div class="cards">
            {#each $scheduledTrips as trip }
            <div class="profile-card-wrapper">
                <CardUserProfile bind:props={trip} />
            </div>
        {/each}
        </div>
    </div>
</div>

<style>
    .user-page-container{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    .user-greeting{
        margin-top: 5rem;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .user-greeting h2{
        font-weight: 600;
    }
    .user-greeting h2 b{
        font-weight: 900;
        color: var(--main-color);
    }

    .usr-img{
        height: 4rem;
        width: 4rem;
        background-color: var(--main-color);
        margin-right: 2rem;
        border-radius: 50%;
    }

    .current-cards{
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        margin-top: 2rem;
        flex-wrap: wrap;
    }
    .current-cards p{
        margin-bottom: 2rem;
        font-weight: 600;
        font-size: 1.2rem;
    }

    .cards{
        display: grid;
        column-gap: 1rem;
        row-gap: 1rem;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
        grid-template-rows: 1fr 1fr;
        margin-bottom: 2rem;
    }

    .profile-card-wrapper{
        text-transform: capitalize;
    }
</style>