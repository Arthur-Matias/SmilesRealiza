<script>
import Card from "../components/Card.svelte"

    const filters = [
        'todos',
        'diversão',
        'cultural',
        'natureza',
        'praia',
        'urbano'
    ]

    const props = [
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
        {
            title: 'rio de janeiro (GIG)',
            
            destination: {
                departure: 'curitiba (CWB)'
            },
            
            packageItems:[
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
                'Lorem impsum sit dolor amet...',
            ],
            
            prices:{
                basePrice: '789,46',
                clubSmilesPrice: '590,68',
            },

            usersReservations:'',
            pictures: [
                'https://images.unsplash.com/photo-1583275479278-7bc72a16c2ae?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=668&q=80',

            ],
        },
    ]

    function handleClick(e, value){
        console.log(value)
    }

</script>

<div class="packages-list-container">
    <header>
        <aside>
            <i class="fas fa-suitcase-rolling"></i>
        </aside>
        <p>
            Internacionais / <b>Todos</b>
        </p>
    </header>
    <div class="filters">
        {#each filters as filter}
            <div on:click={e=>handleClick(e, filter)} class="filter-item {filter === 'todos'?'active':''}">
                <p>{filter}</p>
            </div>
        {/each}
    </div>
    <div class="content">
        {#each props as cardProps}
            <Card bind:cardProps={cardProps} />
        {/each}
    </div>
</div>

<style>
    .packages-list-container{
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
    }

    .packages-list-container > header{
        display: flex;
        align-items: center;
        height: 4rem;
    }
    .packages-list-container > header > aside{
        margin-right: 1rem;
        color: var(--main-color);
        font-size: 1.5rem;
    }

    .filters{
        display: flex;
    }

    .filter-item{
        margin-right: .5rem;
        border: solid 3px var(--dark-gray);
        padding: .2rem .5rem;
        border-radius: 50px;
        cursor: pointer;
        text-transform: capitalize;
    }

    .filter-item:hover, .filter-item.active{
        color: var(--beige);
        background-color: var(--dark-gray);
    }
    
    .content{
        height: 100%;
        width: 100%;
        padding: 2rem;
        display: grid;
        grid-column-gap: 1rem;
        grid-row-gap: 1rem;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        grid-template-rows: 1fr 1fr;
    }


</style>