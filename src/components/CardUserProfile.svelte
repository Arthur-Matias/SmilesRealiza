<script>
import {scheduledTrips} from '../stores.js'
import UserTripModal from './UserTripModal.svelte'

export let isOpen = false;
export let props;

$: modalOpen = isOpen;

console.log($scheduledTrips)
function handleCardAccessClick(){
    setIsOpen(true)
}

function setIsOpen(state){
    console.log("ACESSANDO O TRIP");
    console.log(props);
    modalOpen = state
}

</script>

<UserTripModal 
    bind:isOpen={modalOpen}
    bind:photo={props.pictures[0]}
    bind:prices={props.prices}
    bind:destination={props.destination}
/>
<div on:click={()=>setIsOpen(true)} class="package-card" style="background-image: url({props.pictures[0]});">
    <div class="wrapper">
        <div class="icon">
            <i class="fas fa-suitcase-rolling"></i>
        </div>
        <div class="card-content">
            <h2>{props.title}</h2>
            <p>Saindo de: {props.destination.departure}</p>
            
            <div class="prices">
                <section>
                    <p>Valor total:</p>
                    <h2>{props.prices.clubSmilesPrice}</h2>
                </section>
                
                <div class="trace"></div>
                
                <section>
                    <button on:click="{handleCardAccessClick}">Acessar</button>
                </section>
            </div>
        </div>
    </div>
</div>

<style>
    .package-card{
        position: relative;
        border-radius: .5rem;
        background-repeat: no-repeat;
        background-size: cover;
        height: 100%;
        width: 100%;
        color: var(--white);
        display: flex;
        flex-direction: column;
        transition: ease .2s;
        cursor: pointer;
    }

    .package-card:hover{
        transform: scale(1.15);
        z-index: 100;
    }

    .package-card:hover .icon{
        color: var(--main-color);
    }

    .icon{
        position: absolute;
        font-size: 1.5rem;
    }

    .wrapper{
        padding: 1rem;
        height: 100%;
        width: 100%;
        border-radius: .5rem;
        background-color: rgba(0, 0, 0, .5);
    }
    .card-content{
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: flex-end;
        margin-top: .8rem;
    }

    .card-content button{
        padding: .5rem 1rem;
        border-radius: 4px;

        color: var(--white);

        font-weight: 700;

        background-color: var(--secondary-color);

        cursor: pointer;
    }

    .card-content button:hover{
        filter: opacity(.85);
    }

    .trace{
        display: block;
        background-color: var(--white);
        width: 2px;
        margin: .4rem 1rem;
    }

    .prices{
        display: flex;
    }

    .prices section{
        display: flex;
        flex-direction: column;
        width: 100%;
        height: fit-content;

    }

    .prices section p{
        font-size: .8rem;
    }
</style>