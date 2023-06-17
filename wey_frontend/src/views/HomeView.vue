<template>
<div>
  <wrapper class="flex flex-row  gap-x-5">
    <div>   
      <strong>Почтальон</strong><hr> Самая популярная социальная сеть в России....
      Популярный мессенджер, в котором уже 700 млн активных пользователей, из которых 40 млн из России...              
    </div>
    <div>
      <strong>Наш сервис
      </strong> микроблогов и социальная сеть, в которой пользователи публикуют сообщения, и взаимодействуют с ними. Зарегистрированным пользователям доступна личная переписка и добавление в друзья...
    </div>
    <div>
      <strong>Почтальон</strong> — популярная социальная сеть в качестве продвижения товаров или услуг компаний. Реклама является основным источником дохода для владельцев сети;
        Почтальон предоставляет пользователям возможность оставлять отзывы, так как подписчики могут комментировать публикации, выставлять оценки страницам брендов, чтобы их могли видеть другие. Почтальон может ссылаться на страницу продукта в Twitter, а также отправлять напоминания о событиях. Исследование, проведённое в 2022 году, связывает 84 % «вовлечённости» или кликов с лайками, которые ссылаются на рекламу в Facebook. К 2023 году Почтальон ограничил публикацию контента со страниц компаний и брендов. Изменения в алгоритмах  увеличили аудиторию для неоплачиваемых бизнес-страниц (которые имеют не менее 500 000 «лайков») с 16 % в 2022 году до 42 % в мае 2023 года.
  </div>
  </wrapper>
  <!--  -->
  <div class="p-2 bg-white border border-gray-200 rounded-lg">
        

        <div class="space-y-2">
            <div class="flex items-center justify-start gap-x-5" >
              <div class="flex flex-row" v-for='product in products' :key='product.id'>
                <div class="box">
                    <figure class="w-[150px] rounded-full">
                        <div class="scale">
                            <img :src="product.get_thumbnail" class="scale">
                        </div>
                    </figure>

                    <h3 class="is-size-4">{{ product.name }}</h3>
                    <p class="is-size-6 has-text-grey">${{ product.price }}</p>
                        
                    <router-link v-bind:to="product.get_absolute_url" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Посмотреть</router-link>
                  
                </div>
              </div>
            </div>
        </div>
    </div>
</div>
  
</template>
<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  
  data() {
        return {
            products: []
        }
    },
  mounted() {
      document.title = "Главная | Почтальон"
      this.getFriendSuggestions()
      },
  methods: {
        getFriendSuggestions() {
            axios
                .get('/api/products/latest-products/')
                .then(response => {
                    this.products = response.data
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error', error)
                })
            }
    },
}
</script>
<style scoped>
.image {
    
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    

}
.box {
  background: rgb(217, 218, 215);
  box-shadow: 10px 10px 5px rgb(182, 181, 181);
  opacity: 0.6;
}
.box:hover {
  opacity: 1;
}
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
.scale {
    display: inline-block; /* Строчно-блочный элемент */
    overflow: hidden; /* Скрываем всё за контуром */
   }

.scale img {
    transition: 1s; /* Время эффекта */
    display: block; /* Убираем небольшой отступ снизу */
   }
   .scale img:hover {
    transform: scale(1.2); /* Увеличиваем масштаб */
   }

</style>

