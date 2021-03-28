<script>
    import ReservationTile from './ReservationTile.svelte'
    import {scheduledTrips} from '../stores.js'
    import {goto} from '@sapper/app'

    export let isOpen;

    export let photo;
    export let prices;
    export let destination;
    export let usersReservations;
    export let packageItems;

    export let cardProps;

    function close(){
        isOpen = false;
    }

    function handleReservationClick(){
        $scheduledTrips = [...$scheduledTrips, cardProps]
        console.log($scheduledTrips)
        goto('user_page')
    }
</script>

<div class="package-modal {isOpen?'open':''}">
    <div class="modal-wrapper" >
        <div class="close-btn" on:click={close}>
            <i class="fas fa-times"></i>
        </div>
        <header style="background-image: url({photo});">
            <div>
                <p>Saindo de: {destination.departure.toUpperCase()}</p>
                <h2>{destination.arrival}</h2>
            </div>
        </header>
        <div class="modal-options">
            <div>
                <section>
                    <p>A partir de:</p>
                    <h2><section>R$:</section>{prices.basePrice}</h2>
                </section>
                <section>
                    <p>Clube Smiles:</p>
                    <h2><section>R$:</section>{prices.clubSmilesPrice}</h2>
                </section>
            </div>
            <div class="reservation-btn" on:click={()=>handleReservationClick()}>
                Reserve Já
            </div>
        </div>
        <div class="modal-content">
            <div class="included">
                <header>O que está incluido neste pacote:</header>
                <ul>
                    {#each packageItems as item}
                        <li>{item}</li>
                    {/each}
                </ul>
            </div>
            <div class="reservations">
                <header>
                    Usuários que já <b>realizaram</b> suas reservas
                </header>
                <div class="reservation-content">
                    {#each usersReservations as user}
                        <ReservationTile user={user} />
                    {/each}
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .package-modal{
        position: absolute;
        height: 100vh;
        width: 100vw;
        background: rgba(0, 0, 0, 0.5);
        top: 0;
        left: 0;
        display: none;
        z-index: 200;
        backdrop-filter: blur(3px);
        padding: 5rem;
        overflow: hidden;
    }
    .package-modal.open{
        display: flex;
    }

    .package-modal > div{
        width: 100%;
        height: 100%;
        background-color: var(--white);
        filter: opacity(1);
    }
    .modal-wrapper > header > div{
        height: 100%;
        width: 100%;
        background-color: rgba(0, 0, 0, 0.3);
        color: var(--white);
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-end;
        padding: 1rem 2rem;
    }

    .modal-wrapper > header{
        height: 15rem;
        background-repeat: no-repeat;
        background-size: cover;
        background-position: 50%;
    }

    .modal-wrapper > header > div > p{
        color: var(--soft-gray);
    }
    .modal-wrapper > header > div > h2{
        text-transform: capitalize;
        font-weight: 700;
        font-size: 2rem;
        display: flex;
    }
    
    .modal-options > div > section > h2 > section{
        font-size: 1rem;
        display: inline-block;
    }

    .close-btn{
        position: absolute;
        right: 1rem;
        top: .5rem;
        font-size: 2rem;
        color: red;
        cursor: pointer;
    }
    
    .modal-options{
        display: flex;
        justify-content: space-between;
        padding: 1rem;
    }

    .modal-options > div{
        display: flex;
    }

    .modal-options > div > section{
        margin-right: 2rem;
    }

    .reservation-btn{
        background-color: var(--secondary-color);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem 2rem;
        border-radius: 8px;
        cursor: pointer;
        color: var(--white);
        font-weight: 700;
        transition: ease .2s;
    }

    .reservation-btn:hover{
        filter: opacity(.9);
    }

    .modal-content{
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: space-between;
    }

    .included{
        padding: 1rem;
    }

    .included header{
        color: var(--main-color);
        font-size: 2rem;
    }
    .included ul{
        list-style-type: none;
    }
    .included ul li{
        font-size: 1.5rem;
        color: var(--dark-gray);
        margin-top: 1rem;
    }

    .reservations{
        position: inherit;
        background-color: var(--beige);
        height:25rem;
        margin-right: 1rem;
        width: auto;
        text-align: center;
        display: flex;
        flex-direction: column;
        flex-wrap: nowrap;
        overflow-y: auto;
    }

    .reservations > header{
        font-size: 1.5rem;
        margin: .5rem;
    }
    .reservations > header > b{
        color: var(--main-color)
    }
    .reservation-content{
        padding: 0 1rem;
    }
</style>