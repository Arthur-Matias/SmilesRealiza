<script>
    import ProggressionBar from './ProggressionBar.svelte'
    import {scheduledTrips} from '../stores.js'

    export let isOpen;

    export let photo;
    export let prices;
    export let destination;

    let paymentProgression = 50;
    let miles = 10;
    let buyMiles = 5;

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
        <div class="modal-values">
            <div>
                <p>Valor total</p>
                <div>
                    <p>R$: <b>5.800,68</b></p>
                </div>
            </div>
            <div>
                <p>Valor pago</p>
                <div>
                    <p>R$: <b>3500,00</b></p>
                </div>
            </div>
            <div>
                <p>Valor das parcelas</p>
                <div>
                    <p>R$: <b>500,00</b></p>
                </div>
            </div>
            <div>
                <p>Parcelas restantes</p>
                <div>
                    <p><b>5</b></p>
                </div>
            </div>
        </div>
        <div class="modal-progression">
            <p>
                Progressão:
            </p>

            <ProggressionBar 
                bind:paymentProgression={paymentProgression}
                bind:miles={miles}
                bind:buyMiles={buyMiles}
            />

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
        grid-template-rows: 1fr 2fr 2fr;
    }
    .package-modal.open{
        display: grid;
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

    .close-btn{
        position: absolute;
        right: 1rem;
        top: .5rem;
        font-size: 2rem;
        color: red;
        cursor: pointer;
    }

    .modal-values{
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
    }

    .modal-values > div{
        background-color: var(--beige);
        margin: 0 1rem;
        padding: 1rem .5rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
    }
    .modal-values > div > p{
        display: flex;
        font-size: 1rem;
        align-self: flex-start;
    }

    .modal-values > div > div> p{
        font-size: .8rem;
    }
    .modal-values > div > div> p > b{
        font-size: 1.6rem;
    }

    .modal-values > div > div{
        display: flex;
        align-self: flex-end;
    }
    .modal-progression{
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    .modal-progression p{
        margin: 1rem;
    }
    
</style>